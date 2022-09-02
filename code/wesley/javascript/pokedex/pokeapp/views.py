from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pokemon
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'pokeapp/index.html')

def pokemon(request):
    pokemon = Pokemon.objects.all()
    # paginator = Paginator(pokemon, 20)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    poke = list(pokemon.values('number', 'name', 'image_front'))
    return JsonResponse({'poke': poke},  safe=False)

def fetchPokemon (request, search):
    if request.method == "GET":
        pokemon = Pokemon.objects.filter(name__icontains=search)
        poke = list(pokemon.values("number", "name", "image_front"))
        return JsonResponse({'poke': poke}, safe=False)
    else:    
        pokemon = Pokemon.objects.all()
        poke = list(pokemon.values('number', 'name', 'image_front'))
        return JsonResponse({'poke': poke}, safe=False)