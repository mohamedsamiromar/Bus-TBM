from django.contrib.auth.models import User
from django.core.serializers import serialize
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from swvl.models import Captin, Passenger, Bus


class CreateTrip(serializers.Serializer):
    bus = serializers.CharField()
    captin = serializers.CharField()
    from_address = serializers.CharField()
    from_to = serializers.CharField()
    from_date = serializers.CharField()
    to_date = serializers.CharField()
    price = serializers.IntegerField()
    reserved = serializers.IntegerField()


class TripReservation(serializers.Serializer):
    from_address = serializers.CharField()
    to_address = serializers.CharField()
    reserved_seats = serializers.IntegerField()
    data = serializers.DateTimeField()


class CaptinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Captin
        fields = ['id', 'phone_number', 'email']


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ["id", "phone_number", "email"]


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ['id', 'bus_number', 'color_bus', 'number_seat', 'model_bus']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.IntegerField()


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
