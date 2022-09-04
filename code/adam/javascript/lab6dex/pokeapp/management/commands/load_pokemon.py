# from django.core.management.base import BaseCommand
# import json
# from pokeapp.models import Pokemon

# class Command(BaseCommand):
#     def handle(self, *args, **kwargs):
#         Pokemon.objects.all().delete()
#         # Types.objects.all().delete()

#         # names = ['grass', 'dark', 'dragon', 'poison', 'fire', 'water', 'electric', 'flying', 'bug', 'normal', 'ground', 'fighting', 'psychic', 'rock', 'ghost', 'fairy', 'steel', 'ice']

#         # for name in names:
#         #     type = Types()
#         #     type.name = name
#         #     type.save()

#         with open("./data/pokemon.json") as file:
#             contents = json.loads(file.read())
#             for pokemon in contents['pokemon']:
#                 print(newPokemon = Pokemon())
#                 newPokemon.number = pokemon['number']
#                 newPokemon.name = pokemon['name']
#                 newPokemon.height = pokemon['height']
#                 newPokemon.weight = pokemon['weight']
#                 newPokemon.image_front = pokemon['image_front']
#                 newPokemon.image_back = pokemon['image_back']
#                 newPokemon.save()
                
import json
from django.core.management.base import BaseCommand
from pokeapp.models import Pokemon

class Command(BaseCommand):

    def handle(self, *args, **options):
        Pokemon.objects.all().delete()
        # Type.objects.all().delete()
        # write the code here
        with open("./data/pokemon.json") as file:
            data = json.loads(file.read())

        for creature in data['pokemon']:
            pokemon = Pokemon()
            pokemon.number = creature['number']
            pokemon.name = creature['name']
            pokemon.height = creature['height']
            pokemon.weight = creature['weight']
            pokemon.image_front = creature['image_front']
            pokemon.image_back = creature['image_back']
            pokemon.save()

            # for type in creature['types']:
            #     typeObj, _ = Type.objects.get_or_create(name=type)
            #     pokemon.types.add(typeObj)s

            # pokemon.save()