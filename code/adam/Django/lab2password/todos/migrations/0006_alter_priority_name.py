# Generated by Django 4.0.6 on 2022-08-04 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0005_remove_priority_priority_priority_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priority',
            name='name',
            field=models.CharField(choices=[(0, 'None'), (1, 'Low'), (2, 'Medium'), (3, 'High'), (4, 'Other')], max_length=15),
        ),
    ]
