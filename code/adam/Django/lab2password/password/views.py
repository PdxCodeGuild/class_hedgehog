from django.shortcuts import render
from django.http import HttpResponse
import string
import random

def home(request):
    return render(request, 'password/home.html')



def index(request):
	random_char =  list(string.ascii_letters + string.punctuation + string.digits)
	# number = input("enter number")
	password_length = int(request.POST.get('password_length', 0))
	password = [random.choice(random_char) for i in range(password_length)]
	password = "".join(password)

	context = {
		'password': password
	}

	return render(request, 'password/pass_gen.html', context)
