from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['students_name','image_student', 'bio_student', 'phone_student', 'gender_student']



class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'teacher_name', 'image_teacher', 'experience', 'specialization', 'gender_teacher']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_name']


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [ 'id', 'course_name', 'description', 'price']

class CourseDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    created_by = TeacherSerializer()
    student_course = StudentsSerializer()


    class Meta:
        model = Course
        fields = ['category', 'course_name', 'course_image', 'description', 'price', 'created_at', 'updated_at', 'level_course',
                  'created_by', 'student_course']


class LessonSerializer(serializers.ModelSerializer):
    course_les = CourseListSerializer()
    teacher_les = TeacherSerializer()

    class Meta:
        model = Lesson
        fields = ['id', 'title_name', 'video_url', 'content', 'course_les', 'teacher_les']


class AssignmentSerializer(serializers.ModelSerializer):
    course_as = CourseListSerializer()
    students_as = StudentsSerializer(many=True)

    class Meta:
        model = Assignment
        fields = ['id', 'title_as', 'description_as', 'due_date', 'course_as', 'students_as']



class QuestionsSerializer(serializers.ModelSerializer):
    question_course = CourseListSerializer()

    class Meta:
        model = Questions
        fields = ['id', 'questions_text', 'question_course']




class OptionSerializer(serializers.ModelSerializer):
    questions_op = QuestionsSerializer()

    class Meta:
        model = Option
        fields = ['text_option', 'correct', 'questions_op']





class ExamSerializer(serializers.ModelSerializer):
    course_exam = CourseListSerializer()
    questions = QuestionsSerializer()

    class Meta:
        model = Exam
        fields = ['id', 'title_exam', 'passing_score', 'duration', 'course_exam', 'questions']




class CertificateSerializer(serializers.ModelSerializer):
    student = StudentsSerializer()
    course = CourseListSerializer()

    class Meta:
        model = Certificate
        fields = ['id', 'issued_at', 'certificate_url', 'student', 'course']





class ReviewListSerializer(serializers.ModelSerializer):
    course = CourseListSerializer()

    class Meta:
        model = Review
        fields = ['id', 'rating', 'comment', 'course', 'parent']



class StudentReviewSerializer(serializers.ModelSerializer):
    student_rev = StudentsSerializer()

    class Meta:
        model = StudentReview
        fields = ['id', 'rating_student', 'comment_student', 'student_rev', 'parent_student']



class TeacherReviewSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer()

    class Meta:
        model = TeacherReview
        fields = ['id', 'rating_student', 'comment_teacher', 'teachers', 'parent_teacher']