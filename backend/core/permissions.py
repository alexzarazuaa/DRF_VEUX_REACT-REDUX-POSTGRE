from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
  
    def has_object_permission(self, request, view, obj):

        if obj.owner.user == request.user:
            return True 
        elif request.user.is_superuser and request.user.is_superuser:
            return True

        return False