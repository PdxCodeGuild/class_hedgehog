from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import User, Group

# Create your views here.
def index(request):
    return render(request, 'mapr_app/index.html')

def get_users(request):

    users_query = User.objects.filter(restricted=False, private= False)
    users = []
    for user in users_query:
        users.append({
        'username': user.username,
        'location': {
            'lat': user.location.latitude,
            'lon': user.location.longitude
        }, 
        'groups': list(user.groups.filter(private= False).values('id', 'name'))
        })

    return JsonResponse(users, safe=False)

