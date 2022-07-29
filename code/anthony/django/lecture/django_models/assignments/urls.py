from django.urls import path
from . import views

app_name = "assignments"
# {% url 'assignments:index' %}

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_assignment, name="create")
]
