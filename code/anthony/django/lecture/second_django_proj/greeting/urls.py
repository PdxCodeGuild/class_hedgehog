from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/hello/
    path("", views.index),
    path("form/", views.greet_form),
    # localhost:8000/hello/dave
    path("<str:name>/", views.greet),
]
