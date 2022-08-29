from django.core.management.base import BaseCommand
import json

class load(self, *args, *kwargs):
    try:
        f = open('./pokemon.json')
        contents = json.load(f)
        for i in contents['pokemon']:
            number = contents['number']
            name = contents['name']
            height = contents['height']
            weight = contents['weight']
            image_front = contents['sprites']['front_default']
            image_back = contents['sprites']['back_default']
            types = [type['type']['name'] for type in contents['types']]
       
    except (IOError, OSError) as e:
        print(e)
    finally:
        f.close()