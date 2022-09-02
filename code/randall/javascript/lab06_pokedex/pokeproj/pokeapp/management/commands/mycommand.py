from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        Pokemon.objects.all().delete()
        Type.objects.all().delete()

        with open()