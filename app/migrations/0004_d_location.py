# Generated by Django 5.0.2 on 2024-02-25 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_d_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='D_LOCATION',
            fields=[
                ('code_region_code_departement', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('code_region', models.IntegerField()),
                ('code_departement', models.CharField(max_length=5)),
                ('nom_region', models.CharField(blank=True, default=None, max_length=5, null=True)),
                ('nom_departement', models.CharField(blank=True, default=None, max_length=30, null=True)),
            ],
        ),
    ]
