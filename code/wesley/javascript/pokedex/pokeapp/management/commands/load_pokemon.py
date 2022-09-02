
from django.core.management.base import BaseCommand
import json
from pokeapp.models import Pokemon, PokemonType

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Pokemon.objects.all().delete()
        PokemonType.objects.all().delete()

        # for loop for type in contents:
            # if type is already in Types don't add.
        with open('pokemon.json') as f:
            contents = json.loads(f.read())
        for poke in contents['pokemon']:
            poketype = PokemonType()
            for type in poke['types']:
                try:
                    poketype = PokemonType.objects.get(name = type)
                except PokemonType.DoesNotExist:
                    poketype = PokemonType.objects.create(name = type)

        

        with open('pokemon.json') as f:
            contents = json.loads(f.read())
        for poke in contents['pokemon']:
            pokemon = Pokemon()
            pokemon.number = poke['number']
            pokemon.name = poke['name']
            pokemon.height = poke['height']
            pokemon.weight = poke['weight']
            pokemon.image_front = poke['image_front']
            pokemon.image_back = poke['image_back']
            pokemon.save() 
            for name in poke['types']:
                pokemon.types.add(PokemonType.objects.filter(name=name)[0].id)
            pokemon.save()
             
        
       