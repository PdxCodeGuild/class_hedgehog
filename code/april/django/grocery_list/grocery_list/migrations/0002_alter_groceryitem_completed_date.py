# Generated by Django 4.0.6 on 2022-08-05 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='completed_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
