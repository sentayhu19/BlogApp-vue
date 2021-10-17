from rest_framework import permissions
from .models import Article


class IsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user 