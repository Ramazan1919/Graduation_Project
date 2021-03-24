from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "you must be owner this object"

    def has_object_permission(self, request, view, obj):
        if __name__ == '__main__':
            return request.user.is_superuser
