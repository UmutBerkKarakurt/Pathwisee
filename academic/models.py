from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. User Roles and Custom User Model
class CustomUser(AbstractUser):
    # Roles (Database value, Display name)
    ROLE_CHOICES = (
        ('manager', 'Department Manager'),
        ('teacher', 'Instructor'),
        ('student', 'Student'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    
    # Student number unique
    student_number = models.CharField(max_length=20, blank=True, null=True, unique=True, verbose_name="Student Number")
    
    def __str__(self):
        if self.role == 'student' and self.student_number:
            return f"{self.first_name} {self.last_name} ({self.student_number})"
        return f"{self.first_name} {self.last_name} ({self.get_role_display()})"

# 2. Department Model
class Department(models.Model):
    name = models.CharField(max_length=100, default="Computer Engineering")
    
    def __str__(self):
        return self.name

# 3. Course Model
class Course(models.Model):
    code = models.CharField(max_length=20, unique=True, verbose_name="Course Code") # Ex: CEN101
    name = models.CharField(max_length=100, verbose_name="Course Name")
    instructor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'}, related_name='courses_taught')
    
    def __str__(self):
        return f"{self.code} - {self.name}"

# 4. Learning Outcome (LO)
class LearningOutcome(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='learning_outcomes')
    code = models.CharField(max_length=10, verbose_name="LO Code") # Ex: LO1
    description = models.TextField(verbose_name="Description")
    
    def __str__(self):
        return f"{self.course.code} - {self.code}"