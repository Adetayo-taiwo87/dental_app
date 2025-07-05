from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'student'),
        ('mentor', 'mentor',),
        ('admin', 'admin'),
    )
    role = models.CharField(max_lenght= 10, choices=ROLE_CHOICES, default='student')
    def __str__(self):
        return f"{self.username} ({self.role})"
