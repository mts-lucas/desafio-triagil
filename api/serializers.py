from rest_framework import serializers

from core.models import *


class PokemonSerializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField(source='dex_id')
    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'weight', 'height']
        extra_kwargs = {
            "id": {"read_only": True},
            "weight": {"read_only": True},
            "height": {"read_only": True}
        }



class TeamSerializer(serializers.ModelSerializer):

    pokemons = PokemonSerializer(read_only=True, many=True)

    class Meta:
        model = Team
        fields = ['owner', 'pokemons']
        extra_kwargs = {
            "owner": {"read_only": True},
            "pokemons": {"read_only": True},
        }

