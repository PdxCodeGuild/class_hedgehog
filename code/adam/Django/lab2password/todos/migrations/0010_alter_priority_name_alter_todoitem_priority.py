# Generated by Django 4.0.6 on 2022-08-04 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0009_alter_priority_name_alter_todoitem_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priority',
            name='name',
            field=models.CharField(blank=True, choices=[(0, 'None'), (1, 'Low'), (2, 'Medium'), (3, 'High'), (4, 'Other')], default='other', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='priority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='todos.priority'),
        ),
    ]
