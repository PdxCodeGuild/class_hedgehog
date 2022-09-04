
from django.core.management.base import BaseCommand
import json
# from pokeapp.models import Pokemon, PokemonType
from pokeapp.models import Pokemon

class Command(BaseCommand):

    def handle(self, *args, **options):
        Pokemon.objects.all().delete()
        # PokemonType.objects.all().delete()
        
        with open("pokeapp/management/commands/pokemon.json") as file:
            text = file.read()
            data = json.loads(text)

            for target in data["pokemon"]:

                poke_mon = Pokemon()

                poke_mon.number = target["number"]
                poke_mon.name = target["name"]
                poke_mon.height = (target["height"])/10
                poke_mon.weight = (target["weight"])/10
                poke_mon.image_front = target["image_front"]
                poke_mon.image_back = target["image_back"]
                poke_mon.types = target['types']
                
                
                poke_mon.save()



        