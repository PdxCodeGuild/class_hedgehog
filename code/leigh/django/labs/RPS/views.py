from django.shortcuts import render
import random

def index(request):
    if request.method == "POST":
        human = request.POST.get("choice", "")
        computer = random.choice(["rock", "paper", "scissors"])
        message = ""
        if human == computer:
            message = "tie"
        elif human == "rock" and computer == "paper":
            message = "Computer wins with paper"
        elif human == "rock" and computer == "scissors":
            message = "You win with rock"
        elif human == "paper" and computer == "rock":
            message = "You win with paper"
        elif human == "paper" and computer == "scissors":
            message = "Computer wins with paper"
        elif human == "scissors" and computer == "rock":
            message = "Computer wins with rock"
        elif human == "scissors" and computer == "paper":
            message = "You win with scissors"
        context = {
            "message": message
        }
        return render(request, "RPS/index.html", context)
    return render(request, "RPS/index.html")