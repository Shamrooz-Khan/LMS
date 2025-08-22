from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Custom user model (must be defined first)
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    country = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)

# Course model (uses CustomUser as instructor)
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

