from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
# from rest_framework.pagination import PageNumberPagination
from core.models import *

from .serializers import *
from .utils import pokerequests

# Create your views here.

class TeamsViewList(APIView):

    # pagination_class = PageNumberPagination

        
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
            return Response({"errors": pkm_not_found}, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            # Salva todos os pokemons encontrados
            saved_pkms = []
            for pkm_data in pkms:
                pkm_instance, created = Pokemon.objects.get_or_create(
                    name=pkm_data['name'],
                    dex_id=pkm_data['id'],
                    height=pkm_data['height'],
                    weight=pkm_data['weight']
                )
                saved_pkms.append(pkm_instance)

            # Preenche os dados da equipe
            team_data = {
                'user': request.data['user'],
                'pokemons': saved_pkms
            }
            serializer = TeamPostSerializer(data=team_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamDetail(APIView):


    def get_object(self, pk):
        try:
            return Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            raise Http404('Time não encontrado')

    def get(self, request, pk, format=None):
        team = self.get_object(pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)