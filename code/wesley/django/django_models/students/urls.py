from django.urls import path
from . import views

app_name ="students"

urlpatterns = [
    path('', views.index, name='index'),
    path('students/<int:student_id>/', views.detail, name="detail"),
    path('students/update/<int:student_id>/', views.update_student, name='update')
]
