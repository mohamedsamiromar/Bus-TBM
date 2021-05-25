from rest_framework import permissions, status
from django.contrib.auth.models import User
from swvl.models import Passenger
from rest_framework.response import Response


#
# class IsCaptin(permissions.BasePermission):
#
#     def has_permission(self, request, view):
#         return request.user.captin and request.user.captin.is_authenticated()
#
class IsPassenger(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        return request.user.passenger and request.user.is_authenticated()


# class IsAdmin(permissions.BasePermission):
#
#     def has_permission(self, request, view):
#         return request.user.admin and request.user.is_authenticated()

#
# class PassengerPermission(permissions.IsAuthenticated):
#     def has_permission(self, request, view):
#         passenger = Passenger.objects.filter(user_id=request.user.passenger).filter()
#         if passenger:
#             return Response(status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
