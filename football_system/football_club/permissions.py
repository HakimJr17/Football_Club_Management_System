from rest_framework import permissions

# managers have full access but all other users have read-only access
class IsManagerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        user_role = request.user.profile.role
        if user_role == 'manager':
            return True
        else:
            return request.method in permissions.SAFE_METHODS

# captain, coach, team manager have full access the rest is read only

class IsCaptainOrIsManagerOrIsCoach(permissions.BasePermission):
    def has_permission(self, request, view):
        user_role = request.user.profile.role
        if user_role in ('captain', 'manager', 'coach'):
            return True
        else:
            return request.method in permissions.SAFE_METHODS
    
# club secretary has full access, team manager has read only access, all the rest have no access

class IsClubSecretaryOrManagerReadOnly(permissions.BasePermisision):
    def has_permission(self, request, view):
        user_role = request.user.profile.role
        if user_role == 'secretary':
            return True
        elif user_role == 'manager':
            return request.method in permissions.SAFE_METHODS
        else:
            return False

# captain and team manager have all access, coach and club secretary have read only access, the rest no access

class IsCaptainOrIsManagerOrCoachSecretaryReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        user_role = request.user.profile.role
        if user_role in ('captain', 'manager'):
            return True
        elif user_role in ('coach', 'secretary'):
            return request.method in permissions.SAFE_METHODS
        else:
            return False
        
# captain has all access, manager, club secretary, and coach have read only access

class IsCaptainOrManagerSecretaryCoachReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        user_role = request.user.profile.role
        if user_role == 'captain':
            return True
        elif user_role in ('manager', 'secretary', 'coach'):
            return request.method in permissions.SAFE_METHODS
        else:
            return False

# captain, and coach have all access, manager, club secretary have read only access, the rest have no access

class IsCaptainOrIsCoachOrManagerSecretaryReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        user_role = request.user.profile.role
        if user_role in ('captain', 'coach'):
            return True
        elif user_role in ('manager', 'secretary'):
            return request.method in permissions.SAFE_METHODS
        else:
            return False
