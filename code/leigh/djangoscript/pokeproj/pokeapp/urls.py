from django.urls import path
from . import views

urlpatterns = [
    path("pokemon/<int:page>/<int:limit>", views.pokemon, name="pokemon"),
    path("searchPokemon/<str:search>", views.searchPokemon, name="searchPokemon"),
    path("", views.index, name="index"),
]