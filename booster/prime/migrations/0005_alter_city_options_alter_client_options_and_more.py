# Generated by Django 4.2.4 on 2023-09-05 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0004_fuel_price_fuel_remaining_volume'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Города', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['time_create', 'phone_number', 'name'], 'verbose_name': 'Заказы', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='fuel',
            options={'verbose_name': 'Типы топлива', 'verbose_name_plural': 'Типы топлива'},
        ),
        migrations.AddField(
            model_name='client',
            name='status',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
