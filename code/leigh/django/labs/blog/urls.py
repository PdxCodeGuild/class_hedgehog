from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.logout, name="logout"),
    path('create/', views.create, name="create"),
    path('edit/<int:post_id>', views.edit, name='edit'),
    path('posts/', views.posts, name='posts'),
    path('posts/<int:post_id>', views.post_detail, name='post_detail'),
]
