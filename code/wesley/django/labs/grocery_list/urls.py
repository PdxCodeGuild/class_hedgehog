from django.urls import path
from . import views


app_name = 'grocerylist'
urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:item_id>/', views.update, name='update')
]
