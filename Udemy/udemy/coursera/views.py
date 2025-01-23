from .filters import CourseFilter
from .models import *
from .serializers import *
from rest_framework import viewsets, generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .paginations import PostPagination


class RegisterView(generics.CreateAPIView):
    serializer_class = ProfileSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({'detail': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class TeacherListAPIView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    pagination_class = PostPagination


class TeacherDetailAPIView(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer




class StudentsListAPIView(generics.ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    pagination_class = PostPagination

class StudentsDetailAPIView(generics.RetrieveAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CourseFilter
    search_fields = ['course_name']
    ordering_fields = ['price', 'created_at']
    pagination_class = PostPagination


class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer

class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseListSerializer


class CourseEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDetailAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class AssignmentListAPIView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class QuestionsListAPIView(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class QuestionsDetailAPIView(generics.RetrieveAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class QuestionsCreateAPIView(generics.CreateAPIView):
    serializer_class = QuestionsSerializer


class QuestionsEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class OptionListAPIView(generics.ListAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class OptionDetailAPIView(generics.RetrieveAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class OptionCreateAPIView(generics.CreateAPIView):
    serializer_class = OptionSerializer


class OptionEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class ExamListAPIView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ExamDetailAPIView(generics.RetrieveAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer



class ExamCreateAPIView(generics.CreateAPIView):
    serializer_class = ExamSerializer


class ExamEDITAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class CertificateListAPIView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CertificateDetailAPIView(generics.RetrieveAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer



class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer


class StudentReviewViewSet(viewsets.ModelViewSet):
    queryset = StudentReview.objects.all()
    serializer_class = StudentReviewSerializer


class TeacherReviewViewSet(viewsets.ModelViewSet):
    queryset = TeacherReview.objects.all()
    serializer_class = TeacherReviewSerializer


