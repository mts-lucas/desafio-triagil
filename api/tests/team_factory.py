import factory
from factory.django import DjangoModelFactory
from faker import Faker

from core.models import Team, Pokemon

faker = Faker('pt_BR')
factory.Faker('pt_BR')

class PokemonFactory(DjangoModelFactory):
    name = "pikachu"
    dex_id = 25
    weight = 60
    height = 4

    class Meta:
        model = Pokemon

class TeamFactory(DjangoModelFactory):
    owner = factory.Faker("name")
    pokemons = PokemonFactory()

    class Meta:
        model = Team

def pokemon_to_json(pokemon):

    json_content = {
        "dex_id": pokemon.id,
        "name": pokemon.name,
        "weight": pokemon.pokemons,
        "height": pokemon.pokemons,
    }
    return json_content

def team_to_json(team):

    json_content = {
        "id": team.id,
        "owner": team.name,
        "pokemons": pokemon_to_json(team.pokemons),
    }
    return json_content