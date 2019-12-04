from rest_framework import permissions


class DepartmentPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        Checks permissions
        """
        has_action_permission = False
        if request.user and request.user.is_authenticated:
            if view.action in ['list', 'retrieve', 'by_current_company']:
                has_action_permission = request.user.has_perm('pyplan.view_department')
            elif view.action in ['create']:
                has_action_permission = request.user.has_perm('pyplan.add_department')
            elif view.action in ['update', 'partial_update', 'denied', 'deny_items']:
                has_action_permission = request.user.has_perm('pyplan.change_department')
            elif view.action in ['destroy']:
                has_action_permission = request.user.has_perm('pyplan.delete_department')
        return has_action_permission
