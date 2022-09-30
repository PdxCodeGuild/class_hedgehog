from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('examiner/', views.examiner, name='examiner'),
    path('about/', views.about, name='about'),
    # path('login_logout/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]
