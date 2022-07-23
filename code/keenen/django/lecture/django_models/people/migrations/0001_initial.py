# Generated by Django 4.0.6 on 2022-07-21 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('is_close_friend', models.BooleanField(default=False)),
            ],
        ),
    ]
