from rest_framework import serializers

from swvl.models import Captin, Passenger


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