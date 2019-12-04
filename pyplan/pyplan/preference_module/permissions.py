from rest_framework import permissions


class PreferenceModulePermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        Checks permissions
        """
        has_action_permission = False
        if request.user and request.user.is_authenticated:
            if view.action in ['list', 'retrieve']:
                has_action_permission = request.user.has_perm('pyplan.view_preferencemodule')
            elif view.action in ['create']:
                has_action_permission = request.user.has_perm('pyplan.add_preferencemodule')
            elif view.action in ['update', 'partial_update']:
                has_action_permission = request.user.has_perm('pyplan.change_preferencemodule')
            elif view.action in ['destroy']:
                has_action_permission = request.user.has_perm('pyplan.delete_preferencemodule')
        return has_action_permission
