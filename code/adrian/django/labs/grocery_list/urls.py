from django.urls import path
from . import views

app_name = 'grocery_list'
# {% url 'grocery_list:index' %}

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_item, name="create"),
    # path(''),
]
