
from django.core.management.base import BaseCommand
import json
from pokeapp.models import Pokemon

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Pokemon.objects.all().delete()
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
            pokemon.types = poke['types']
            pokemon.save()  
        
       