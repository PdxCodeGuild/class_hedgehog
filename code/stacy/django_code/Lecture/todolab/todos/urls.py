from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup")
]


# no app_name
# {% url 'signup' %}

# if you have an app_name
# {% url 'todos:signup' %}