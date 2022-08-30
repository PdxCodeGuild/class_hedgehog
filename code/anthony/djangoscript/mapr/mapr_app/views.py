import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .models import User, Group, Location

# Create your views here.
def index(request):
    return render(request, "mapr_app/index.html")


def get_users(request):
    # query = User.objects.filter(restricted=False, private=False).values('username', 'location__latitude', 'location__longitude', 'groups__name')
    # users = list(query)
    limit = request.GET.get("limit", 50)
    users_query = User.objects.filter(restricted=False, private=False)[:limit] #Limit response to 50 users

    users = []
    for user in users_query:
        users.append({
            "username": user.username,
            "location": {
                "lat": user.location.latitude,
                "lon": user.location.longitude
            },
            "groups": list(user.groups.filter(private=False).values("id", "name"))
        })

    return JsonResponse(users, safe=False)

# @login_required('login')
def get_groups(request):
    print(request.user)
    groups = list(Group.objects.filter(private=False, users__username=request.user).values())
    return JsonResponse({"data": groups})


def get_group_by_id(request, group_id):
    group = Group.objects.get(id=group_id)
    users = list(group.users.filter(private=False, restricted=False).values("username", "id", "location__latitude", "location__longitude"))
    return JsonResponse({"data": users})


def login(request):
    if request.method == "GET":
        return render(request, "mapr_app/login.html")
    elif request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username", "")
        password = data.get("password", "")

        user = auth.authenticate(request, username=username, password=password)
        if user == None:
            return JsonResponse({"message": "Invalid username or password."})
        else:
            auth.login(request, user)
            return JsonResponse({"message": "ok"})
