from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """Grants access to users with role 'admin' or superusers."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.role == 'admin' or request.user.is_superuser
        )

class IsMember(BasePermission):
    """Grants access only to users with role 'member'."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'member'