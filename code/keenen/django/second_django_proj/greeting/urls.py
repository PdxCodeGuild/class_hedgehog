from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('form/', views.greet_form),
    path('<str:name>/', views.greet),
]