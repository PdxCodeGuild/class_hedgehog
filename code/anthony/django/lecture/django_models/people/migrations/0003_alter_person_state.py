# Generated by Django 4.0.6 on 2022-07-26 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_state_person_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='people.state'),
        ),
    ]
