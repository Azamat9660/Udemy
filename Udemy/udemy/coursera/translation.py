from .models import Course, Teacher, Students, Category, Exam, Questions, Assignment, Lesson, Option
from modeltranslation.translator import TranslationOptions, register


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description' )

@register(Teacher)
class TeacherTranslationOptions(TranslationOptions):
    fields = ('experience', 'specialization', )

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(Students)
class StudentsTranslationOptions(TranslationOptions):
    fields = ('bio_student',  )

@register(Exam)
class ExamComboTranslationOptions(TranslationOptions):
    fields = ('title_exam', )

@register(Questions)
class QuestionsTranslationOptions(TranslationOptions):
    fields = ('questions_text', )




@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('title_as', 'description_as', )


@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title_name', 'content', )

@register(Option)
class OptionTranslationOptions(TranslationOptions):
        fields = ('text_option' ,)


