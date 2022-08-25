from django.core.management.base import BaseCommand

from mapr_app.models import User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User.objects.filter(is_staff=False).delete()
        for x in range(10):
            User.objects.create_user(f'testUser{x}', '', 'password')
            print(f"created user testUser{x}")
