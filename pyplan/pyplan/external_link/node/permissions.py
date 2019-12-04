from rest_framework import permissions

SAFE_METHODS = ['POST', 'HEAD', 'OPTIONS']

class NodeExternalLinkPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        It lets unauthorized users to do GET, HEAD and OPTIONS
        """
        if request.method in SAFE_METHODS:
            return True
        has_action_permission = False
        if request.user and request.user.is_authenticated:
            if view.action == 'list' or view.action == 'retrieve':
                has_action_permission = request.user.has_perm('pyplan.view_nodeexternallink')
            elif view.action == 'create':
                has_action_permission = request.user.has_perm('pyplan.add_nodeexternallink')
            elif view.action == 'update' or view.action == 'partial_update' or view.action == 'by_node_id':
                has_action_permission = request.user.has_perm('pyplan.change_nodeexternallink')
            elif view.action == 'destroy':
                has_action_permission = request.user.has_perm('pyplan.delete_nodeexternallink')
        return has_action_permission
