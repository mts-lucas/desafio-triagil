from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Pokemon(models.Model):

    dex_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=32)
    weight = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Pokemon'
        verbose_name_plural = 'Pokemons'


class Team(models.Model):
    owner = models.CharField(max_length=32)
    pokemons = models.ManyToManyField(Pokemon)

    def validate_max_pokemons(self):
        max_pokemons = 6
        if self.outros_modelos.count() > max_pokemons:
            raise ValidationError(f"Só é permitido um máximo de {max_pokemons} pokemons por time.")

    def __str__(self):
        return f'Time de {self.owner}'

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    