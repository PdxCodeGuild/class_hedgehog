from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.index),
    path('goodbye/', views.goodbye),
    path('hello/<str:name>/', views.hello),
]