

from . import views
from django.urls import path

app_name = "assignments"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_assignment, name="create")
]

