from .models import Course
from django_filters import FilterSet



class CourseFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
            'price': ['gt', 'lt'],
            'level_course': ['exact'],
            'category': ['exact'],

        }