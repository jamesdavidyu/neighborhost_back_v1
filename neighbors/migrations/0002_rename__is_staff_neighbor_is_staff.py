# Generated by Django 5.0.6 on 2024-06-09 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbor',
            old_name='_is_staff',
            new_name='is_staff',
        ),
    ]
