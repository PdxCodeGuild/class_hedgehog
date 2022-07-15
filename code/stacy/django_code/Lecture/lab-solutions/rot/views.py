from django.shortcuts import render, HttpResponse
import string
# Create your views here.

def index(request):
    rotated = ""
    phrase = request.POST.get("phrase", "")
    amount = int(request.POST.get("amount", 0))
    characters = [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits, " "]
    for letter in phrase:
        for char in characters:
            if letter in char:
                location = char.index(letter)
                rotated += char[(location + amount) % len(char)]
    context = {
        "rotated": rotated
    }
    return render(request, 'rot/index.html', context)
