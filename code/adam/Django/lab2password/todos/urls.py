from django.urls import path
from . import views



app_name = "todos"

# {% url 'todos:(name)' %}

urlpatterns = [
    path("", views.index, name="index"),
]
