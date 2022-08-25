from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import User

# Create your views here.
def index(request):
    return HttpResponse("ok")


def get_users(request):
    query = User.objects.filter(restricted=False, private=False).values('username', 'location', 'groups')
    users = list(query)
    return JsonResponse(users, safe=False)