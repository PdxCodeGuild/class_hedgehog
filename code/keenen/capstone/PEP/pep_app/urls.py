from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('examiner/', views.examiner, name='examiner'),
    path('state_search/', views.state_search, name='state_search'),
]
