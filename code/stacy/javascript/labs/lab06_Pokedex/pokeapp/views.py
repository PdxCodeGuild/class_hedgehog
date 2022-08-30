from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pokemon
import json

# Create your views here.
def index(request):

    return 

def pokemon(request):
    # Create a view pokemon that gets a list of Pokemon out of the database and turns them into a dictionary to be passed to JsonResponse. Verify this works by going to localhost:8000/pokemon/ in your browser and seeing a list of pokemon in JSON
    pokemon = Pokemon.objects.all()
    data = list(pokemon.values("number", "name"))
    return JsonResponse({"data": data}, safe=False)
