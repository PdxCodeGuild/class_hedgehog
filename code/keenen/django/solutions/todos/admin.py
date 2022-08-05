from django.contrib import admin

from .models import TodoItem, Priority

admin.site.register(Priority)
admin.site.register(TodoItem)


