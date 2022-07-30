from django.urls import path
from . import views

app_name = 'shorty'
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.shortyurl, name='shorty'),


]