from django.urls import path
from . import views

app_name = 'grocery_list'
# {% url 'grocery_list:index' %}

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_item, name="create"),
    path('complete/<int:item_id>', views.completed, name='completed'),
    path('delete/<int:item_id>', views.delete_item, name='delete'),
]
