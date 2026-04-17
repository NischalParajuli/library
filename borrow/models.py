# Import Django's models module for defining database models
from django.db import models
# Import User model from accounts app for user relationship
from accounts.models import User
# Import Book model from books app for book relationship
from books.models import Book

# Define the BorrowRecord model to track book borrowing transactions
class BorrowRecord(models.Model):
    # Define choices for the status field
    STATUS_CHOICES = (
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
    )

    # Foreign key to User model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrow_records')
    # Foreign key to Book model
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrow_records')

    # Date when the book was borrowed
    borrow_date = models.DateField(auto_now_add=True)
    # Due date for returning the book
    due_date = models.DateField(default='2025-01-01')
    # Date when the book was returned
    return_date = models.DateField(null=True, blank=True)
    # Status of the borrow record
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='borrowed')

    # String representation of the model instance
    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.status})"