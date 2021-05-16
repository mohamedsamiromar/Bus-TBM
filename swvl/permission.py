from rest_framework import permissions


class IsCaptin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.captin and request.user.captin.is_authenticated()


class IsPassenger(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.passenger and request.user.passenger.is_authenticated()


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.admin and request.user.admin.is_authenticated()

