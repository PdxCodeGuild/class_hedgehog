from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('people.urls')),
    path('assignments/', include('assignments.urls')),
    path('students/', include('students.urls')),
    path('user/', include('users.urls'))
]
