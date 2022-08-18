from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('create/', views.create, name='create'),
    path('logout/', views.logout, name='logout'),
    path('post/<int:post_id>', views.post, name='post')
]