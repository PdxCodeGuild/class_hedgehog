from django.shortcuts import render
from django.http import HttpResponse
import string
# Create your views here.

def index(request):
    if request.method == "POST":
        phrase = request.POST.get("phrase", "")
        message = ""
        rot_phrase = ""
        try:
            rot = int(request.POST.get("rot", 0))
            char_sets = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation, " "]
            for letter in phrase:
                for char_set in char_sets:
                    if letter in char_set:
                        loc = char_set.index(letter)
                        rot_phrase += char_set[(loc + rot) % len(char_set)]
            context = {
                "message": message,
                "rot_phrase": rot_phrase,
            }
        except (ValueError, TypeError):
            message = "Rot amount must be a whole number"
            context = {
                "message": message,
                "rot_phrase": rot_phrase,
            }
        return render(request, "rot/index.html", context)
    return render(request, "rot/index.html")