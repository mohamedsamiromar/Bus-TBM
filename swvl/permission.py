from rest_framework import permissions, status
from django.contrib.auth.models import User
from swvl.models import Passenger
from rest_framework.response import Response


#
# class IsCaptin(permissions.BasePermission):
#
#     def has_permission(self, request, view):
#         return request.user.captin and request.user.captin.is_authenticated()

# class IsAdmin(permissions.BasePermission):
#
#     def has_permission(self, request, view):
#         return request.user.admin and request.user.is_authenticated()


class PassengerPermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        passenger = Passenger.objects.filter(user=request.user).first()
        if passenger:
            return True
        return False



