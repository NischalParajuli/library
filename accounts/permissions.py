# Import BasePermission for custom permissions
from rest_framework.permissions import BasePermission

# Custom permission class for admin users
class IsAdmin(BasePermission):
    """Grants access to users with role 'admin' or superusers."""
    def has_permission(self, request, view):
        # Check if user is authenticated and has admin role or is superuser
        return request.user.is_authenticated and (
            request.user.role == 'admin' or request.user.is_superuser
        )

# Custom permission class for member users
class IsMember(BasePermission):
    """Grants access only to users with role 'member'."""
    def has_permission(self, request, view):
        # Check if user is authenticated and has member role
        return request.user.is_authenticated and request.user.role == 'member'