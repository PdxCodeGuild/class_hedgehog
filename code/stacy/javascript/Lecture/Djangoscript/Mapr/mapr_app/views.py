from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# from django.core import serializers
import json
from .models import User, Group

def index(request):
    return render(request, "mapr_app/index.html")

def get_users(request):
    #### it kinda works
    # query = User.objects.filter(restricted=False, private=False).values("username", 'location__latitude', 'location__longitude', 'groups__name')
    # users = list(query)
    #### for use with serializer
    # data = serializers.serialize("json", User.objects.all())
    # users = json.loads(data)
    users_query = User.objects.filter(restricted=False, private=False)[:50]
    users = []
    for user in users_query:
        users.append({
            "username": user.username,
            "location": {
                "lat": user.location.latitude,
                "long": user.location.longitude
            },
            "groups": list(user.groups.filter(private=False).values("id", "name")),
        })
    return JsonResponse(users, safe=False)
    
def get_groups(request):
    groups = list(Group.objects.filter(private=False).values())
    return JsonResponse({"data": groups})

def get_group_by_id(request, group_id):
    group = Group.objects.get(id=group_id)
    users = list(group.users.filter(private=False, restricted=False).values("username", "id", "location__latitude", "location__longitude"))
    return JsonResponse({"data": users})