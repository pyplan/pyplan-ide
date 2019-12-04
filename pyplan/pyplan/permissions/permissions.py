from rest_framework import permissions


class PermissionPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        Checks permissions
        """
        has_action_permission = False
        if request.user and request.user.is_authenticated and view.action in ['list']:
            has_action_permission = request.user.has_perm('auth.view_permission')
        return has_action_permission
