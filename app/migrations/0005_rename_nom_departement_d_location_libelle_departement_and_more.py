# Generated by Django 5.0.2 on 2024-02-25 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_d_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='d_location',
            old_name='nom_departement',
            new_name='libelle_departement',
        ),
        migrations.RenameField(
            model_name='d_location',
            old_name='nom_region',
            new_name='libelle_region',
        ),
    ]
