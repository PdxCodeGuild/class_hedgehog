from django.shortcuts import redirect, render
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from pokeapp.models import Pokemon


# Create your views here.
def poke_app(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
  
    pokesearch = Pokemon.objects.filter(Q(name__icontains=q) | Q(number__icontains=q))
   

    msg = "Hello Turtle Island!"

    context = {
        "msg": msg,
        "pokesearch": pokesearch
    }
    return render(request, 'pokeapp/index.html', context)



def pokemon(request):
    pokemon_query = Pokemon.objects.all()

    pokemon_el = []
    for pokemon in pokemon_query:
        pokemon_el.append({
            "number": pokemon.number,
            "name": pokemon.name,
            "height": pokemon.height,
            "weight": pokemon.weight,
            "image_front": pokemon.image_front,
            "image_back": pokemon.image_back
        })

    return JsonResponse({"data":pokemon_el}, safe=False)