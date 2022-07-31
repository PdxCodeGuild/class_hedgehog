from django.urls import path
from . import views

app_name = 'shorty'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.shortyurl, name='shorty'),
    path('create/', views.shortyurl, name='shorty'),

]