from django.urls import path
from . import views

urlpatterns = [
    path('', views.poke_app, name="home")
]
