from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pokemon

# Create your views here.
def index(request):
    return render(request, 'pokeapp/index.html')

def pokemon(request):
    if request.method == "GET":
        search = request.GET.get("search")
        if search != None:
            pokemon = Pokemon.objects.filter(name__icontains='mew')
            data = list(pokemon.values("number", "name", "image_front"))
        else:    
            pokemon = Pokemon.objects.all()
            poke = list(pokemon.values('number', 'name', 'image_front'))
            return JsonResponse({'poke': poke}, safe=False)