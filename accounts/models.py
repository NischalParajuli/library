# Import Django's models module for defining database models
from django.db import models
# Import AbstractUser to extend Django's built-in User model
from django.contrib.auth.models import AbstractUser

# Custom User model extending Django's AbstractUser
class User(AbstractUser):
    # Define choices for user roles
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('member', 'Member'),
    )
    # Role field to distinguish between admin and member users
    role = models.CharField(max_length=20, choices=ROLE_CHOICES,)