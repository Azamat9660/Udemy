from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


GENDER_CHOICES = (
    ('мужкой', 'мужкой'),
    ('женский', 'женкский'),
    ('другой', 'другой')
)

class Profile(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile')
    bio = models.TextField()
    phone_number = PhoneNumberField(region='KG')
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator (14),
                                                       MaxValueValidator (50)], null=True, blank=True)

    def __str__(self):
        return self.username

class Students(models.Model):
    students_name = models.CharField(max_length=32)
    image_student = models.ImageField(upload_to='image_students', null=True, blank=True)
    bio_student = models.TextField()
    phone_student = PhoneNumberField(region='KG')
    gender_student = models.CharField(max_length=16, choices=GENDER_CHOICES)

    def __str__(self):
        return self.students_name

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=32)
    image_teacher = models.ImageField(upload_to='image_teacher')
    experience = models.TextField()
    specialization = models.CharField(max_length=32)
    gender_teacher = models.CharField(max_length=16, choices=GENDER_CHOICES)

    def __str__(self):
        return  self.teacher_name


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)


    def __str__(self):
        return self.category_name



class Course(models.Model):
    course_name = models.CharField(max_length=32)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    student_course = models.ForeignKey(Students, on_delete=models.CASCADE)

    LEVEL_CHOICES = (
        ('начальный', 'начальный'),
        ('средний', 'средний'),
        ('продвинутый', 'продвинутый'),
    )

    level_course = models.CharField(max_length=16, choices=LEVEL_CHOICES)

    def __str__(self):
        return self.course_name


class  Lesson(models.Model):
    title_name = models.CharField(max_length=64)
    video_url = models.FileField(upload_to='lesson_video', null=True, blank=True)
    content = models.TextField()
    course_les = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher_les = models.OneToOneField(Teacher, on_delete=models.CASCADE)


    def __str__(self):
        return self.title_name

class Assignment(models.Model):
    title_as = models.CharField(max_length=32)
    description_as = models.TextField()
    due_date = models.DateField()
    course_as = models.ForeignKey(Course, on_delete=models.CASCADE)
    students_as = models.ManyToManyField(Students, related_name='student_assignment')

    def __str__(self):
        return self.title_as

class Questions(models.Model):
    questions_text = models.TextField()
    question_course = models.ForeignKey(Course, on_delete=models.CASCADE)


    def __str__(self):
        return self.questions_text

class Option(models.Model):
    questions_op = models.ForeignKey(Questions, on_delete=models.CASCADE)
    text_option = models.CharField(max_length=50)
    correct = models.BooleanField()

    def __str__(self):
        return self.text_option

class Exam(models.Model):
    title_exam = models.CharField(max_length=32)
    course_exam = models.ForeignKey(Course, on_delete=models.CASCADE)
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    passing_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    duration = models.DurationField(default=timedelta(minutes=100))

    def __str__(self):
        return self.title_exam

class Certificate(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateField()
    certificate_url = models.FileField(upload_to='certificate')


    def __str__(self):
        return f'{self.student}  -  {self.course}'

class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating =models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)


    def __str__(self):
        return f'{self.course} - {self.rating}'

class StudentReview(models.Model):
    student_rev = models.ForeignKey(Students, on_delete=models.CASCADE)
    rating_student = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    parent_student = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    comment_student = models.TextField(null=True, blank=True)


    def __str__(self):
        return f'{self.student_rev} -  {self.rating_student}'

class TeacherReview(models.Model):
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    rating_student = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    parent_teacher = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    comment_teacher = models.TextField(null=True, blank=True)


    def __str__(self):
        return f'{self.teachers} - {self.rating_student}'

