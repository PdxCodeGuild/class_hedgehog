from django.shortcuts import render
import random

# Create your views here.
def index(request):
    print(request.POST)
    user = request.POST.get('my_choice', None)
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    outcome = ''


    if user == computer:
        outcome = 'It was a tie'
    elif user == 'rock':
        if computer == 'scissors':
            outcome = 'You Win!'
        elif computer =='paper':
            outcome = 'You Lose!'
    elif user == 'paper':
        if computer == 'rock':
            outcome = 'You Win!'
        elif computer =='scissors':
            outcome = 'You Lose!'
    elif user == 'scissors':
        if computer == 'paper':
            outcome = 'You Win!'
        elif computer =='rock':
            outcome = 'You Lose!'
    
    context = {
        'outcome': outcome, 
        'computer': computer,
        'user': user,
    }
        
    return render(request, 'RPS/index.html', context)