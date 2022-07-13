from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.1:8000/hello
    path('hello/', views.index),
    path('goodbye/', views.goodbye),
    path('hello/<str:name>/', views.hello)
]