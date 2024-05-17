from rest_framework.permissions import BasePermission, SAFE_METHODS


class AllowPostWithoutAuth(BasePermission):
    """
    Custom permission to allow unauthenticated users to create a user (POST)
    but require authentication for other request types.
    """

    def has_permission(self, request, view):
        # Allow all POST requests
        if request.method == 'POST':
            return True
        # Require authentication for other methods
        return request.user and request.user.is_authenticated
