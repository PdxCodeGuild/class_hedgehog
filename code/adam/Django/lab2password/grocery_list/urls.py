from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='groceries'),
    path('list/<str:pk>/', views.grocery_list, name='check-list'),
    path('create/', views.create_list, name= 'create-list'),
    path('update/<str:pk>/', views.update_list, name= 'update-list'),
    path('delete/<str:pk>/', views.delete_list, name= 'delete-list'),
]
