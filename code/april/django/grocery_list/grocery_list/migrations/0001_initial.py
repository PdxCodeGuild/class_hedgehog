# Generated by Django 4.0.6 on 2022-08-05 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_description', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('completed_date', models.DateTimeField(auto_now=True, null=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
