from _ast import Is
from datetime import datetime

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Trip, Booking
from .serializer import TripReservation, AssignTrip
from .permission import IsCaptin, IsPassenger, IsAdmin


class WhereFrom(APIView):
    # permission_classes = [IsPassenger, ]

    def post(self, request):
        serializer = TripReservation(data=request.data)
        if serializer.is_valid():
            from_address = serializer.validated_data['from_address']
            to_address = serializer.validated_data['to_address']
            reserved_seats = serializer.validated_data['reserved_seats']
            data = serializer.validated_data['data']
            if data is None or from_address is None or to_address is None or reserved_seats is None:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            trip = Trip.objects.filter(from_date__lts=data, to_date__gte=data, from_address=from_address,
                                       to_address=to_address)
            return Response(serializer, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk=None):
        trip = Trip.objects.get(pk=pk)
        trip.delete()
        return Response(status=status.HTTP_201_CREATED)


class CreateTrip(APIView):
    # permission_classes = [IsAdmin]

    def post(self, request):
        from_address = request.data.get('from_address')
        to_address = request.data.get('to_address')
        bus = request.data.get('bus')
        captin = request.data.get('captin')
        from_date = request.data.get('from_date')
        to_date = request.data.get('to_date')
        price = request.data.get('price')
        reserved = request.data.get('reserved')
        trip = Trip()
        trip.from_address = from_address
        trip.to_address = to_address
        trip.Bus = bus
        trip.Captin = captin
        trip.from_date = from_date
        trip.to_date = to_date
        trip.price = price
        trip.reserved = reserved
        trip.save()
        return Response(trip, status=status.HTTP_201_CREATED)

    def delete(self, pk=None):
        trip = Trip.objects.get(pk=pk)
        trip.delete()
        return {"Massage": "Trip Is deleted"}

    def update(self, request, pk):
        trip_id = Trip.objects.get(pk=pk)

        bus = request.data.get("bus")
        captin = request.data.get("captin")
        from_address = request.data.get("from_address")
        to_address = request.data.get("to_address")
        from_date = request.data.get("from_date")
        to_date = request.data.get("to_date")
        price = request.data.get('price')
        reserved = request.data.get('reserved')

        trip_id.bus = bus
        trip_id.captin = captin
        trip_id.from_address = from_address
        trip_id.to_address = to_address
        trip_id.from_date = from_date
        trip_id.to_date = to_date
        trip_id.price = price
        trip_id.reserved = reserved
        trip_id.save()
        return trip_id


class Reserved(APIView):
    # permission_classes = [IsPassenger]

    def post(self, request, pk=None):
        trip = Trip.objects.get(pk=pk)
        reserved_seats = request.data.get('reserved_seats')
        if trip.reserved + reserved_seats >= trip.bus.number_seat:
            return {"Massage": "Bus Is Full"}
        else:
            reserved_seats -= trip.reserved
            booking = Booking()
            booking.from_address = trip.from_address
            booking.to_address = trip.to_address
            booking.date = datetime.now()
            booking.price = trip.price
            booking.trip = trip
            price = trip.price * reserved_seats
            booking.total_price = price * reserved_seats
            booking.reserved_seats = reserved_seats
            booking.save()
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, pk=None):
        booking = Booking.objects.get(pk=pk)
        booking.delete()
        return Response(status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        trip = Booking.objects.get(pk=pk)
        reserved = request.data.get("reserved_seats")
        if trip.reserved + reserved >= trip.bus.number_seat:
            return {"Massage": "Bus Is Full"}
        else:
            reserved -= trip.reserved_seats
            booking = Booking()
            booking.trip = trip
            booking.reserved_seats = reserved
            booking.from_address = trip.from_address
            booking.to_address = trip.to_address
            booking.date = datetime.now()
            price = trip.price * reserved
            booking.price = trip.price
            booking.total_price = price
            booking.save()
            return Response(status=status.HTTP_201_CREATED)


class TakeTrip(APIView):

    def get(self, request):
        captin = request.data.get('captin')
        trip = Trip.objects.filter(captin=captin)
        return Response(trip, status=status.HTTP_201_CREATED)
