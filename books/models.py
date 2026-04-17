# Import Django's models module for defining database models
from django.db import models

# Define the Book model to represent books in the library
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)

    # Unique book number
    book_no = models.CharField(max_length=20, unique=True)
    # Availability status
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
  