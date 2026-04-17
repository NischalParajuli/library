# Import serializers from Django REST Framework
from rest_framework import serializers
# Import User model
from .models import User

# Serializer for User model - converts data to/from JSON
class UserSerializer(serializers.ModelSerializer):
    # Password field is write-only for security
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        # Create user with hashed password using create_user method
        user = User.objects.create_user(**validated_data)
        return user