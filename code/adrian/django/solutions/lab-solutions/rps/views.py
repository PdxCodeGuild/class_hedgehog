from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def index(request):
    choices = ['rock', 'paper', 'scissors']
    user_choice = request.POST.get('user_choice', '').lower()
    cpu_choice = random.choice(choices)
    message = ''

    if user_choice == cpu_choice:
        message = "It's a tie!"
    elif user_choice == 'rock':
        if cpu_choice == 'paper':
            message = "You Win! Rock beats Scissors!"
        else:
            message = "You Lose! Paper beats Rock!"
            
    elif user_choice == 'paper':
        if cpu_choice == 'rock':
            message = "You Win! Paper beats Rock!"
        else:
            message = "You Lose! Scissors beats paper"

    elif user_choice == 'scissors':
        if cpu_choice == 'paper':
            message = "You Win! Scissors beats Paper"
        else:
            message = "You Lose! Rock beats scissors"


    context = {
        'title': 'Rock, Paper, Scissors',
        'message': message
    }

    return render(request, 'rps/index.html', context)