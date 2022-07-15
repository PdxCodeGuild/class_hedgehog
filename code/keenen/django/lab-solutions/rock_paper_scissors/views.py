from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def index(request):
    computer = random.choice(['rock', 'paper', 'scissors'])
    user = request.POST.get('weapon', '')

    if user == computer:
        outcome = 'Tie'
    elif user == 'paper' and not computer == 'scissors':
        outcome = 'Victory!'
    elif user == 'rock' and not computer == 'paper':
        outcome = 'Victory!'
    elif user == 'scissors' and not computer == 'rock':
        outcome = 'Victory!'
    else:
        outcome = "You've been defeated by the computer!"
    
    
    context = {
        'welcome': 'Welcome to Rock, Paper, Scissors!',
        'choice': 'Please select rock, paper, or scissors from the menu below.',
        'outcome': outcome
    }    

    return render (request, 'rock_paper_scissors/index.html', context)
   


