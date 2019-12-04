from rest_framework import permissions


class ActivityPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        Checks permissions
        """
        has_action_permission = False
        if request.user and request.user.is_authenticated:
            if view.action in ['list', 'retrieve']:
                has_action_permission = request.user.has_perm('pyplan.view_activity')
            elif view.action in ['create']:
                has_action_permission = request.user.has_perm('pyplan.add_activity')
            elif view.action in ['update', 'partial_update']:
                has_action_permission = request.user.has_perm('pyplan.change_activity')
            elif view.action in ['destroy']:
                has_action_permission = request.user.has_perm('pyplan.delete_activity')
        return has_action_permission
