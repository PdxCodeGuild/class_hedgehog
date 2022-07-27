from . import views
from django.urls import path

app_name = 'students'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:student_id>', views.detail, name="detail")
]
