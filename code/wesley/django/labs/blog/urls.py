from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_post, name='create'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('edit/<int:post_id>', views.editpost, name='edit'),
    path('view/<int:post_id>', views.viewpost, name='view'),
]


