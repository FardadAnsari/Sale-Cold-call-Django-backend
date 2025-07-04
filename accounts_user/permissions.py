from rest_framework.permissions import BasePermission



class Member(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            (request.user.is_active or request.user.is_superuser)
        )


class SelfInfo(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return False
        if request.user.is_superuser:
            return True
        return obj.user_id == request.user