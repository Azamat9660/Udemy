from rest_framework import permissions
from rest_framework.permissions import BasePermission



class CheckOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class CreateReview(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role == 'client'

class CheckStudent(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.student

class CheckTeacher(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.teacher