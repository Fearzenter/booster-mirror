# Generated by Django 4.2.4 on 2023-09-05 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0003_city_fuel_alter_client_fuel_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuel',
            name='price',
            field=models.FloatField(default=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fuel',
            name='remaining_volume',
            field=models.FloatField(default=50),
            preserve_default=False,
        ),
    ]
