from django.core.management.base import BaseCommand
import json
from pokeapp.models import Pokemon, Types

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Pokemon.objects.all().delete()
        Types.objects.all().delete()

        names = ['grass', 'dark', 'dragon', 'poison', 'fire', 'water', 'electric', 'flying', 'bug', 'normal', 'ground', 'fighting', 'psychic', 'rock', 'ghost', 'fairy', 'steel', 'ice']

        for name in names:
            type = Types()
            type.name = name
            type.save()

        f = open('pokeapp/management/commands/pokemon.json')
        contents = json.load(f)
        for pokemon in contents['pokemon']:
            newPokemon = Pokemon()
            newPokemon.number = pokemon['number']
            newPokemon.name = pokemon['name']
            newPokemon.height = int(pokemon['height']) / 10
            newPokemon.weight = int(pokemon['weight']) / 10
            newPokemon.image_front = pokemon['image_front']
            newPokemon.image_back = pokemon['image_back']
            newPokemon.save()
            for name in pokemon['types']:
                newPokemon.types.add(Types.objects.filter(name=name)[0].id)
            newPokemon.save()