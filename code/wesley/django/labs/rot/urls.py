from django.urls import path
from . import views

app_name = 'rot'
urlpatterns = [
    path('', views.index)
]
