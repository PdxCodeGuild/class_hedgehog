from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.index, name="index"),
    path("save_todo", views.save_todo_item, name="create"),
    path("complete/<int:todo_id>", views.complete, name="complete"),
    path("delete/<int:todo_id>", views.delete, name="delete"),
]