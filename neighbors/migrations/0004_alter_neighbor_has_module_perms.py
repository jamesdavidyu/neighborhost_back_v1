# Generated by Django 5.0.6 on 2024-06-09 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbors', '0003_neighbor_has_module_perms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbor',
            name='has_module_perms',
            field=models.CharField(default='view'),
        ),
    ]
