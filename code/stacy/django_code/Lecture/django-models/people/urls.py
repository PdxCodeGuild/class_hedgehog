from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("person/<int:person_id>/", views.person_detail, name="person_detail"),
    path("update/<int:person_id>/", views.update_person, name="update_person"),
    path("delete/<int:person_id>/", views.delete_person, name="delete_person")
]