from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# from django.core import serializers
import json

from .models import User

def index(request):
    return HttpResponse("Ok")

def get_users(request):
    #### it kinda works
    # query = User.objects.filter(restricted=False, private=False).values("username", 'location__latitude', 'location__longitude', 'groups__name')
    # users = list(query)

    #### for use with serializer
    # data = serializers.serialize("json", User.objects.all())
    # users = json.loads(data)

    users_query = User.objects.filter(restricted=False, private=False)
    users = []
    for user in users_query:
        users.append({
            "username": user.username,
            "location": {
                "lat": user.location.latitude,
                "long": user.location.longitude
            },
            "groups": list(user.groups.fliter(private=False).values("id", "name")),
        })
    return JsonResponse(users, safe=False)