import factory
from factory.django import DjangoModelFactory
from faker import Faker

from core.models import Pokemon, Team

faker = Faker('pt_BR')
factory.Faker('pt_BR')

class PokemonFactory(DjangoModelFactory):
    name = 'fwefwf'
    dex_id = 2323
    weight = factory.Faker('random_number', digits=2)
    height = factory.Faker('random_number', digits=1)

    class Meta:
        model = Pokemon

class TeamFactory(DjangoModelFactory):
    owner = factory.Faker('name')

    @factory.post_generation
    def pokemons(self, create, extracted, **kwargs):
        if not create:
            # Atribuição direta, portanto, apenas retornamos
            return

        if extracted:
            # Se uma lista de pokémons foi fornecida, adicionamos ao time
            for pokemon in extracted:
                self.pokemons.add(pokemon)

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
    return {
        "id": team.id,
        "owner": team.owner,
        "pokemons": [pokemon.id for pokemon in team.pokemons.all()]
    }
