from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Если пользователь не автор, то только для чтения"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
