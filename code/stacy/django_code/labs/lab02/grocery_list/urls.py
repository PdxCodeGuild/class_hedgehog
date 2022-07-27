from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("item/<int:item_id>", views.item_detail, name="item_detail"),
    path("update/<int:item_id>/", views.update, name="update"),
    path("delete/<int:item_id>/", views.delete, name="delete")
]

