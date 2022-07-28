# Generated by Django 4.0.6 on 2022-07-27 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0011_alter_grocerylist_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocerylist',
            name='completed',
            field=models.CharField(choices=[('Complete', 'Complete'), ('Incomplete', 'Incomplete')], default='Incomplete', max_length=12),
        ),
    ]
