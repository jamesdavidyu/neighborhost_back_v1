# Generated by Django 5.0.6 on 2024-06-09 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbors', '0007_neighbor_is_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbor',
            old_name='neighbor_id',
            new_name='id',
        ),
    ]
