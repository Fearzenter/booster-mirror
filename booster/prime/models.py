from django.db import models
from django.urls import reverse

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО')
    phone_number = models.CharField(max_length=255, verbose_name='Номер телефона')
    car_model = models.CharField(max_length=255, verbose_name='Авто')
    color = models.CharField(max_length=255, verbose_name='Цвет')
    gos_number = models.CharField(max_length=255, verbose_name='Гос-номер')
    fuel_type = models.ForeignKey('Fuel', on_delete=models.PROTECT, verbose_name='Топливо')
    volume = models.FloatField(verbose_name='Объем поставки')
    price = models.FloatField(verbose_name='Сумма к оплате')
    payment = models.CharField(max_length=255, verbose_name='Способ оплаты')
    city = models.CharField(max_length=255, verbose_name='Город')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    delivery_time = models.DateTimeField(verbose_name='Дата доставки')
    status = models.BooleanField(verbose_name='Статус')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.phone_number}"

    def get_absolute_url(self):
        return reverse('estimate_check', {'check': self.pk})

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'
        ordering = ['time_create', 'phone_number', 'name']


class Fuel(models.Model):
    type = models.CharField(max_length=255, verbose_name='Тип топлива')
    price = models.FloatField(verbose_name='Цена (1 л.)')
    remaining_volume = models.FloatField(verbose_name='Объем на складе')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Типы топлива'
        verbose_name_plural = 'Типы топлива'
        ordering = ['id']


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Города'
        verbose_name_plural = 'Города'
        ordering = ['id']