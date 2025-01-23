from rest_framework import permissions


class CheckCreateCourse(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.level_course in ['teacher', 'admin']:
            return True
        return False



class CheckUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.profile_status == 'admin':
            return True
        return False