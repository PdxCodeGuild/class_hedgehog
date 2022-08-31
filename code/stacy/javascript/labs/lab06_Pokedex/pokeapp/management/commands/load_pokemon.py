from django.core.management.base import BaseCommand
from pokeapp.models import Pokemon, PokemonType
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        Pokemon.objects.all().delete()
        f = open("pokeapp\management\commands\pokemon.json")
        contents = json.load(f)
        # for x in range(len(contents['pokemon'])):
        for x in range(5):
            poke = Pokemon()
            poke.number = contents["pokemon"][x]["number"]
            poke.name = contents['pokemon'][x]['name']
            poke.height = contents["pokemon"][x]["height"] / 10
            poke.weight = contents["pokemon"][x]["weight"] / 10
            poke.image_front = contents["pokemon"][x]["image_front"]
            poke.image_back = contents["pokemon"][x]["image_back"]
            poke.save()
            pokemon_types = contents["pokemon"][x]["types"]
            for type in pokemon_types:
                newtype = PokemonType.objects.get(name=type)
                poke.types.add(newtype)
            poke.save()


