from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError
import datetime as dt

from .models import *


COLOR_CHOICES = [
    "Черный",
    "Серебристый",
    "Белый",
    "Красный",
    "Желтый",
    "Синий",
    "Зеленый",
    "Фиолетовый",
    "Оранжевый"
]

FUEL_CHOICES = [
    "АИ 92",
    "АИ 95",
    "АИ 98",
    "АИ 100",
    "ДТ Зима",
    "ДТ Лето",
    "СУГ",
    "Метан"
]

PAYMENT_CHOICES = [
    "Наличные",
    "Карта",
    "Перевод",
    "QR-код"
]

'''HOUR_CHOICES = [
                   (None, '------')] + \
               [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(0, 24)
                ]'''


class newClientForm(forms.Form):
    name = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=255)
    car_model = forms.CharField(max_length=255)
    color = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=COLOR_CHOICES
    )
    gos_number = forms.CharField(max_length=255)
    fuel_type = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FUEL_CHOICES
    )
    volume = forms.FloatField()
    payment = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=PAYMENT_CHOICES
    )
    city = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    '''delivery_time = forms.Select(
        choices=HOUR_CHOICES
    )'''


    def clean_volume(self):
        volume = self.cleaned_data['volume']
        if volume < 20:
            raise ValidationError('Минимальный объем 20л')
        return volume

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if len(phone_number) > 11:
            raise ValidationError('Нестандартный номер телефона')
        return phone_number

    def clean_gos_number(self):
        gos_number = self.cleaned_data['gos_number']
        if len(gos_number) > 9:
            raise ValidationError('Нестандартный гос номер')
        return gos_number
