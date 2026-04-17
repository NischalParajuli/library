# Import serializers module from Django REST Framework
from rest_framework import serializers
# Import the Book model to create serializer for it
from .models import Book

# Define serializer for Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'book_no', 'is_available']