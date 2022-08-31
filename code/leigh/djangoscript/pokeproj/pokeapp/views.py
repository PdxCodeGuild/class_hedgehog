from django.shortcuts import render
from django.http import JsonResponse
from .models import Pokemon
from django.core.paginator import Paginator

# Create your views here.
def searchPokemon(request, search):
    pokemon_query = Pokemon.objects.filter(name__contains=search)
    pokemons = []
    for pokemon in pokemon_query:
        pokemons.append({
            "name": pokemon.name,
            "number": pokemon.number,
            "height": pokemon.height,
            "weight": pokemon.weight,
            "image_front": pokemon.image_front,
            "image_back": pokemon.image_back,
            "types": list(pokemon.types.all().values("id", "name"))
        })
    return JsonResponse({"data": pokemons})
   

def pokemon(request, page, limit):
    pokemon_query = Pokemon.objects.all()
    p = Paginator(pokemon_query, limit)
    pokemons = []
    for pokemon in p.page(page):
        pokemons.append({
            "name": pokemon.name,
            "number": pokemon.number,
            "height": pokemon.height,
            "weight": pokemon.weight,
            "image_front": pokemon.image_front,
            "image_back": pokemon.image_back,
            "types": list(pokemon.types.all().values("id", "name"))
        })
    return JsonResponse({"data": pokemons})

def index(request):
    return render(request, 'pokeapp/index.html')