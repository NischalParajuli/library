# Import serializers from Django REST Framework
from rest_framework import serializers
# Import BorrowRecord model
from .models import BorrowRecord

# Serializer for BorrowRecord model
class BorrowRecordSerializer(serializers.ModelSerializer):
    # Display username instead of user ID
    user = serializers.StringRelatedField()
    # Display book title instead of book ID
    book = serializers.StringRelatedField()

    class Meta:
        model = BorrowRecord
        fields = ['id', 'user', 'book', 'borrow_date', 'due_date', 'return_date', 'status']