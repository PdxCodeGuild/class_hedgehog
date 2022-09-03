from django.shortcuts import render
from .models import Pokemon
from django.http import JsonResponse

def index(request):
    return render(request, "pokeapp/index.html")


def pokemon(request):
    query = request.GET.get("query", "")
    pokemon= Pokemon.objects.filter(name__contains=f"{query}").order_by("id")
    poke_list = []
    for poke_mon in  pokemon:
        poke_list.append({
            "number": poke_mon.number,
            "name": poke_mon.name,
            "height": poke_mon.height,
            "weight": poke_mon.weight,
            "image_front": poke_mon.image_front,
            "image_back": poke_mon.image_back,
            "types": poke_mon.types
        })
    return JsonResponse({"poke_mon": poke_list})