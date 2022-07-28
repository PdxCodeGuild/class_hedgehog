from django.urls import path
from . import views
app_name = 'people'

urlpatterns = [
    path('', views.index, name='index'),
    path('person/<int:person_id>/', views.person_detail, name='person_detail'),
    path('update/<int:person_id>', views.update, name='update'),
    path('delete/<int:person_id>/', views.delete, name='delete')
]
