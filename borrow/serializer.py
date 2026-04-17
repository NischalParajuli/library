from rest_framework import serializers
from .models import BorrowRecord

class BorrowRecordSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Shows Username instead of id
    book = serializers.StringRelatedField()  

    class Meta:
        model = BorrowRecord
        fields = ['id', 'user', 'book', 'borrow_date', 'due_date', 'return_date', 'status']