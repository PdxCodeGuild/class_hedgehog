# Generated by Django 4.0.6 on 2022-07-24 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0005_grocerylist_items_delete_groceryitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Items',
            new_name='Item',
        ),
        migrations.RenameField(
            model_name='grocerylist',
            old_name='status',
            new_name='complete',
        ),
    ]
