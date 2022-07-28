from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='groceries'),
    path('create/', views.create_list, name= 'create_list'),
]
