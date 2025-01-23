from django.urls import path, include
from rest_framework import routers
from .views import *

routers = routers.SimpleRouter()
routers.register(r'review', ReviewViewSet, basename = 'review')
routers.register(r'student_rev', StudentReviewViewSet, basename='student_rev')
routers.register(r'teacher_rev', TeacherReviewViewSet, basename='teacher_rev')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(routers.urls)),
    path('users/', ProfileListAPIView.as_view(), name='users_list'),
    path('user/<int:pk>/', ProfileDetailAPIView.as_view(), name='users_detail'),
    path('teacher/', TeacherListAPIView.as_view(), name='teacher_list'),
    path('teacher/<int:pk>/', TeacherDetailAPIView.as_view(), name='teacher_detail'),
    path('students/', StudentsListAPIView.as_view(), name='student_list'),
    path('student/<int:pk>/', StudentsDetailAPIView.as_view(), name='student_detail'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('course/', CourseListAPIView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),
    path('course/create/', CourseCreateAPIView.as_view(), name='course_create'),
    path('course/create/<int:pk>/', CourseEDITAPIView.as_view(), name='course_edit'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson_detail'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/create/<int:pk>/', LessonEDITAPIView.as_view(), name='lesson_edit'),
    path('question/', QuestionsListAPIView.as_view(), name='question_list'),
    path('question/<int:pk>/', QuestionsDetailAPIView.as_view(), name='question_detail'),
    path('question/create/', QuestionsCreateAPIView.as_view(), name='question_create'),
    path('question/create/<int:pk>/', QuestionsEDITAPIView.as_view(), name='question_edit'),
    path('option/', OptionListAPIView.as_view(), name='option_list'),
    path('option/<int:pk>/', OptionDetailAPIView.as_view(), name='option_detail'),
    path('option/create/', LessonCreateAPIView.as_view(), name='option_create'),
    path('option/create/<int:pk>/', OptionEDITAPIView.as_view(), name='option_edit'),
    path('exam/', ExamListAPIView.as_view(), name='exam_list'),
    path('exam/<int:pk>/', ExamDetailAPIView.as_view(), name='exam_detail'),
    path('exam/create/', ExamCreateAPIView.as_view(), name='exam_create'),
    path('exam/create/<int:pk>/', ExamEDITAPIView.as_view(), name='exam_edit'),
    path('certificate/', CertificateListAPIView.as_view(), name='certificate_list'),
    path('certificate/<int:pk>/', CertificateDetailAPIView.as_view(), name='certificate_detail'),
    path('assignment/', AssignmentListAPIView.as_view(), name='assignment_list')
]