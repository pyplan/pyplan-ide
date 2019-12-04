from rest_framework import permissions


class CompanyPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        Checks permissions
        """
        has_action_permission = False
        if request.user and request.user.is_authenticated:
            if view.action in ['list']:
                has_action_permission = request.user.has_perm('pyplan.list_companies')
            elif view.action in ['retrieve', 'preferences', 'preference_by_code', 'list_with_groups_and_depts']:
                has_action_permission = request.user.has_perm('pyplan.view_company')
            elif view.action in ['create']:
                has_action_permission = request.user.has_perm('pyplan.add_company')
            elif view.action in ['update', 'partial_update']:
                has_action_permission = request.user.has_perm('pyplan.change_company')
            elif view.action in ['destroy']:
                has_action_permission = request.user.has_perm('pyplan.delete_company')
        return has_action_permission
