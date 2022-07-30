from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('saveform/', views.save_todo_item, name='save'),
    path('complete/<int:todo_id>', views.complete, name='complete'),
    path('delete/<int:todo_id>', views.delete, name='delete')
]
