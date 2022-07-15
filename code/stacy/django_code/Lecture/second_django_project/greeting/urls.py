from django.urls import path 
from . import views

urlpatterns = [
    # localhost:8000/hello/
    path("", views.index),
    # localhost:8000/hello/whatshisname
    path("form/", views.greet_form),
    path("<str:name>/", views.greet),
    # path()
]