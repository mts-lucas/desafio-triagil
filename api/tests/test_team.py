import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .team_factory import TeamFactory, team_to_json


class TeamsViewTests(APITestCase):
    def setUp(self):

        self.team = TeamFactory()

    def test_get_all(self):
        url = reverse("team-list")
        response = self.client.get(url)
        self.assertEquals(status.HTTP_200_OK, response.status_code)

        expected_content = [team_to_json(self.team)]
        response_data = json.loads(response.content)
        self.assertEqual(response_data[0], expected_content)

    def test_post_not_found(self):
        url = reverse("team-list")

        team_json = {
            "user": "ash",
            "pokemons": ["sfsffs"],
            }

        response = self.client.post(url, data=team_json)
        self.assertEquals(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_post(self):

        url = reverse("team-list")

        team_json = team_to_json(self.team)
        response = self.client.post(url, data=team_json)
        response_json = json.loads(response.content)

        id_value = response_json["id"]
        team_json["id"] = id_value
        self.assertEquals(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(team_json, response_json)

    def test_get_one(self):
        url = reverse("team-detail", args=[self.team.id])
        response = self.client.get(url)
        response_data = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        expected_content = team_to_json(self.team)
        self.assertEqual(response_data, expected_content)


    def test_get_one_not_found(self):

        url = reverse("team-detail", args=8374)

        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)