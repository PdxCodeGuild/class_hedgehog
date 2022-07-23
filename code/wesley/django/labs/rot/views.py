import string
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    phrase = request.POST.get('phrase', '')
    rotated_phrase = ''
    amount = int(request.POST.get('amount', 0))
    characters = [string.printable]

    for letter in phrase:
        for char in characters:
            if letter in char:
                location = char.index(letter)
                rotated_phrase += char[(location + amount) % len(char)]

    context = {
        "rotated_phrase": rotated_phrase
    }            
    return render(request, 'rot/index.html', context)