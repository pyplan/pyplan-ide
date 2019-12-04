from rest_framework import permissions


class ReportExternalLinkPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        Checks permissions
        """
        has_action_permission = False
        if request.user and request.user.is_authenticated:
            if view.action == 'list' or view.action == 'retrieve':
                has_action_permission = request.user.has_perm('pyplan.view_reportexternallink')
            elif view.action == 'create':
                has_action_permission = request.user.has_perm('pyplan.add_reportexternallink')
            elif view.action == 'update' or view.action == 'partial_update':
                has_action_permission = request.user.has_perm('pyplan.change_reportexternallink')
            elif view.action == 'destroy':
                has_action_permission = request.user.has_perm('pyplan.delete_reportexternallink')
        return has_action_permission
