from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='grocery'),

    path('details/<int:grocery_id>/', views.details, name='details'),

    path('delete/<int:grocery_id>/', views.delete, name='delete'),

    path('complete/<int:grocery_id>', views.complete, name='complete'),


]
