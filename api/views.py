from django.http import Http404
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from core.models import *

from .serializers import *
from .utils import pokerequests

# Create your views here.

class TeamsListView(APIView):

    pagination_class = PageNumberPagination

        
    def get(self, request, format=None):

        teams = Team.objects.all()
        
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(teams, request)
        serializer = TeamSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request, format=None):
        data = request.data.copy()
        pkm_not_found, pkms = pokerequests.do_requests(data['pokemons'])

        if pkm_not_found:
            return Response({"errors": pkm_not_found}, status=status.HTTP_404_NOT_FOUND)
        
        else:
            pkm_list = []
            for pkm_data in pkms:
                pkm_instance, created = Pokemon.objects.get_or_create(
                    name=pkm_data['name'],
                    dex_id=pkm_data['id'],
                    height=pkm_data['height'],
                    weight=pkm_data['weight']
                )
                pkm_list.append(pkm_instance)

            team = Team.objects.create(owner=data["user"])
            team.pokemons.add(*pkm_list)
            serializer = TeamSerializer(team)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class TeamDetailView(APIView):


    def get_object(self, pk):
        try:
            return Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        team = self.get_object(pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)
    
class ApiRootView(APIView):
    def get(self, request, format=None):
        data = {
            'team-list': reverse('team-list', request=request, format=format),
            'team-detail': reverse('team-detail', request=request, args=[1], format=format),
        }
        return Response(data)