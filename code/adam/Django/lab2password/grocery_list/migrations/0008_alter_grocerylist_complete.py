# Generated by Django 4.0.6 on 2022-07-24 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0007_alter_grocerylist_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocerylist',
            name='complete',
            field=models.BooleanField(choices=[('Completed', 'Completed'), ('Incomplete', 'Incomplete')], null=True),
        ),
    ]
