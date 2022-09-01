from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pokemon
import json

# Create your views here.
def index(request):

    return render(request, "pokeapp/index.html")

def pokemon(request):
    if request.method == "GET":
        search_term = request.GET.get("searchTerm")
        if search_term != None:
            pokemon = Pokemon.objects.filter(name__contains=f"{search_term}")
            data = list(pokemon.values("number", "name", "image_front"))
            return JsonResponse({"data": data}, safe=False)
        else:
            pokemon = Pokemon.objects.all()
            data = list(pokemon.values("number", "name", "image_front"))
            return JsonResponse({"data": data}, safe=False)
   