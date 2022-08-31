
from django.core.management.base import BaseCommand
import json
from pokeapp.models import Pokemon

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            pokemon = Pokemon.objects.all()
            with open('pokemon.json', encoding= 'utf-8') as f:
                print(f.read())
                contents = json.loads(f.read())
            # for i in contents['pokemon']:
            #     pokemon.number = contents['number']
            #     pokemon.name = contents['name']
            #     pokemon.height = contents['height']
            #     pokemon.weight = contents['weight']
            #     pokemon.image_front = contents['sprites']['front_default']
            #     pokemon.image_back = contents['sprites']['back_default']
            #     pokemon.types = contents['types'].join(",")
            #     pokemon.save()  
        
        except (IOError, OSError) as e:
            print(e)
        finally:
            f.close()