# Generated by Django 4.0.5 on 2022-09-02 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='wight',
            new_name='weight',
        ),
    ]
