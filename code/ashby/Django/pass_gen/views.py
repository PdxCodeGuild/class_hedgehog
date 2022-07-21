from string import ascii_lowercase
from django.shortcuts import render
from django.http import HttpResponse
import string
import random

from .forms import password_form
# Create your views here.

char_list=string.ascii_letters + string.punctuation +string.digits

def index(request):

    if request.method == 'POST':
        form = password_form(request.POST)
        if form.is_valid():
            try:
                password_length = int(request.POST.get('char_num', 0))
                password = ""
                for x in range(password_length):
                    password += random.choice(char_list)
                context = {'password' : ''.join(password), 'form':form}
            except:
                return render(request, 'pass_gen/index.html', {'form': password_form(), 'error': 'error'})
    else: 
            context ={ 'form': password_form()}

    return render(request, 'pass_gen/index.html', context)

