from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),

    path('', views.index, name="index"),
    path('create/', views.createPost, name="create-post"),
    # path('update-post/<str:pk>/', views.updatePost, name="update-post"),
    path('delete-post/<str:pk>/', views.deletePost, name="delete-post"),

]
