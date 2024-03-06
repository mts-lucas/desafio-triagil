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
        self.assertEqual(response_data["results"][0], expected_content[0])

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

        team_json = {
            "user": "italo",
            "pokemons": ["tauros", "pichu"],
        }
        data = json.dumps(team_json)
        response = self.client.post(url, data=data, content_type='application/json')
        response_json = json.loads(response.content)

        self.assertEquals(status.HTTP_201_CREATED, response.status_code)

    def test_get_one(self):
        url = reverse("team-detail", args=[self.team.id])
        response = self.client.get(url)
        response_data = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        expected_content = team_to_json(self.team)
        self.assertEqual(response_data, expected_content)


    def test_get_one_not_found(self):

        url = reverse("team-detail", args=[8989])

        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)