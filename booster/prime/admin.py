from django.contrib import admin

# Register your models here.
from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'car_model', 'gos_number', 'price', 'time_create', 'status')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'phone_number')
    list_editable = ('status',)
    list_filter = ('status', 'time_create', 'city')


class FuelAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'price', 'remaining_volume')
    list_display_links = ('id', 'type')


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Client, ClientAdmin)
admin.site.register(Fuel, FuelAdmin)
admin.site.register(City, CityAdmin)