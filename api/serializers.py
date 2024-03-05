from rest_framework import serializers

from core.models import *


class PokemonSerializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField(source='dex_id')
    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'weight ', 'weight ']
        extra_kwargs = {
            "id": {"read_only": True},
            "weight": {"read_only": True},
            "height": {"read_only": True}
        }

class TeamSerializer(serializers.ModelSerializer):

    pokemons = PokemonSerializer()

    class Meta:
        model = Team
        fields = ['owner', 'pokemons']
        extra_kwargs = {
            "owner": {"read_only": True},
            "pokemons": {"read_only": True},
        }

class TeamPostSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='owner', max_length=32)
    pokemons = serializers.ListField(serializers.CharField(max_length=32))

    class Meta:
        model = Team
        fields = ['user', 'pokemons']

    def validate_pokemons(self, value):
        max_pokemons = 6
        if len(value) > max_pokemons:
            raise serializers.ValidationError(f"Só é permitido um máximo de {max_pokemons} pokemons por time.")
        return value

