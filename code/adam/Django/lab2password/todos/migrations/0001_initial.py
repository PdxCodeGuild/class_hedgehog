# Generated by Django 4.0.6 on 2022-08-04 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(choices=[(0, 'None'), (1, 'Low'), (2, 'Medium'), (3, 'High'), (4, 'Other')], default=0, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now=True)),
                ('completed_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
