from rest_framework import serializers

from prime.models import *


class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = ('type', 'price', 'remaining_volume')


class ClientSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=255)
    car_model = serializers.CharField(max_length=255)
    color = serializers.CharField(max_length=255)
    gos_number = serializers.CharField(max_length=255)
    fuel_type_id = serializers.IntegerField()
    volume = serializers.FloatField()
    price = serializers.FloatField()
    payment = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
    delivery_time = serializers.DateTimeField()
    status = serializers.BooleanField(default=False)
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.phone_number = validated_data.get("phone_number", instance.name)
        instance.car_model = validated_data.get("car_model", instance.name)
        instance.color = validated_data.get("color", instance.name)
        instance.gos_number = validated_data.get("gos_number", instance.name)
        instance.fuel_type_id = validated_data.get("fuel_type_id", instance.name)
        instance.volume = validated_data.get("volume", instance.name)
        instance.price = validated_data.get("price", instance.name)
        instance.payment = validated_data.get("payment", instance.name)
        instance.city = validated_data.get("city", instance.name)
        instance.address = validated_data.get("address", instance.name)
        instance.delivery_time = validated_data.get("delivery_time", instance.name)
        instance.status = validated_data.get("status", instance.name)
        instance.time_update = validated_data.get("time_update", instance.name)
        instance.save()
        return instance

