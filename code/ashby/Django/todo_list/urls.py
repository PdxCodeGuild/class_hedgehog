from django.urls import path
from . import views
app_name='todo_list'

urlpatterns = [
    path('', views.index, name='index'),

    path('detail/<int:todo_id>', views.detail, name='detail'),

    path('create/', views.create, name='create'),
    
    path('delete/<int:todo_id>', views.delete, name='delete'),

    path('complete/<int:todo_id>', views.complete, name='complete'),
]
