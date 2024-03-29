# Generated by Django 4.1 on 2022-08-30 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('image_front', models.CharField(max_length=200)),
                ('image_back', models.CharField(max_length=200)),
                ('types', models.CharField(max_length=50)),
            ],
        ),
    ]
