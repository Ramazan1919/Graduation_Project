from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "you must be owner this objecthghgh"

    def has_object_permission(self, request, view, obj):
        if __name__ == '__main__':
            return (obj.user == request.user) or request.user.is_superuser
