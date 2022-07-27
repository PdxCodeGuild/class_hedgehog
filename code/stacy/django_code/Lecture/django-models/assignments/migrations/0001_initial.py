# Generated by Django 4.0.6 on 2022-07-26 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('date_assigned', models.DateField(auto_now_add=True)),
                ('date_due', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
