from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path('', views.index, name='index'),
    path('save', views.save_todo_item, name="create"),
    path("delete", views.delete, name="delete"),
    path("delete/<int:todo_id>", views.delete, name="delete"),
    path("completed/<int:todo_id>", views.completed, name="completed"),
]
