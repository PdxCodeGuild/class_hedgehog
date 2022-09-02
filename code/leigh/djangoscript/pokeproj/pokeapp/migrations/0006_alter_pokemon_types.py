# Generated by Django 4.1 on 2022-08-30 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0005_alter_pokemon_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='types',
            field=models.ManyToManyField(blank=True, null=True, related_name='pokemon', to='pokeapp.types'),
        ),
    ]
