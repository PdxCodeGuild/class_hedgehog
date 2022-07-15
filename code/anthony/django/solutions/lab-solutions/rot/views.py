from django.shortcuts import render
from django.http import HttpResponse
import string


def index(request):
    phrase = request.POST.get('phrase', '')
    rotated_phrase = ''
    amount = int(request.POST.get('amount', 0))
    characters = [string.ascii_letters, string.digits, string.punctuation, " "]

    for letter in phrase:
        for char in characters:
            if letter in char:
                location = char.index(letter)
                rotated_phrase += char[(location + amount) % len(char)]

    context = {
        "rotated_phrase": rotated_phrase
    }

    return render(request, 'rot/index.html', context)
