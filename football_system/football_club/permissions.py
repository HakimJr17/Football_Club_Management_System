from rest_framework import permissions

# managers have full access but all other users have read-only access
class IsManagerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # This line checks if the user's role collection contains a role named 'Manager' which is in line with the changes I have made in the models.py file where a user can have several roles. 
        if request.user.profile.roles.filter(name='Manager').exists():
            return True
        else:
            return request.method in permissions.SAFE_METHODS

# captain, team manager, coach have full access the rest is read only

class IsCaptainOrIsManagerOrIsCoach(permissions.BasePermission):
    def has_permission(self, request, view):
        allowed_roles = ['Manager', 'Captain', 'Coach']
        if request.user.profile.roles.filter(name__in=allowed_roles).exists():
            return True
        else:
            return request.method in permissions.SAFE_METHODS
    
# club secretary has full access, team manager has read only access, all the rest have no access

class IsClubSecretaryOrManagerReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.profile.roles.filter(name = 'Secretary').exists():
            return True
        elif request.user.profile.roles.filter(name = 'Manager').exists():
            return request.method in permissions.SAFE_METHODS
        else:
            return False

# captain and team manager have all access, coach and club secretary have read only access, the rest no access

class IsCaptainOrIsManagerOrCoachSecretaryReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        full_access_allowed_roles = ['Captain', 'Manager']
        read_access_allowed_roles = ['Coach', 'Secretary']
        if request.user.profile.roles.filter(name__in=full_access_allowed_roles).exists():
            return True
        elif request.user.profile.roles.filter(name__in=read_access_allowed_roles).exists():
            return request.method in permissions.SAFE_METHODS
        else:
            return False
        
# captain has all access, manager, club secretary, and coach have read only access
        
class IsCaptainOrManagerSecretaryCoachReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        full_access_allowed_roles = ['Captain']
        read_access_allowed_roles = ['Manager', 'Secretary', 'Coach']
        if request.user.profile.roles.filter(name__in=full_access_allowed_roles).exists():
            return True
        elif request.user.profile.roles.filter(name__in=read_access_allowed_roles).exists():
            return request.method in permissions.SAFE_METHODS
        else:
            return False
        
# captain, and coach have all access, manager, club secretary have read only access, the rest have no access
        
class IsCaptainOrIsCoachOrManagerSecretaryReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        full_access_allowed_roles = ['Captain', 'Coach']
        read_access_allowed_roles = ['Manager', 'Secretary']
        if request.user.profile.roles.filter(name__in=full_access_allowed_roles).exists():
            return True
        elif request.user.profile.roles.filter(name__in=read_access_allowed_roles).exists():
            return request.method in permissions.SAFE_METHODS
        else:
            return False