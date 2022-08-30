import json
from django.core.management.base import BaseCommand
from pokeapi.models import Type, Pokemon

class Command(BaseCommand):

    def handle(self, *args, **options):
        Pokemon.objects.all().delete()
        Type.objects.all().delete()
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

            for type in creature['types']:
                typeObj, _ = Type.objects.get_or_create(name=type)
                pokemon.types.add(typeObj)

            pokemon.save()
