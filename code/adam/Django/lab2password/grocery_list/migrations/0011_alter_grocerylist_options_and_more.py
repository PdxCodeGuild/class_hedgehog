# Generated by Django 4.0.6 on 2022-07-24 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0010_alter_grocerylist_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grocerylist',
            options={},
        ),
        migrations.RenameField(
            model_name='grocerylist',
            old_name='description',
            new_name='details',
        ),
    ]
