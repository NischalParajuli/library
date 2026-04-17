# Import APIView for custom API views
from rest_framework.views import APIView
# Import Response and status for API responses
from rest_framework.response import Response
from rest_framework import status
# Import permissions
from rest_framework.permissions import AllowAny
# Import User model and serializer
from .models import User
from .serializer import UserSerializer
# Import swagger decorator for API documentation
from drf_yasg.utils import swagger_auto_schema

# View for user registration
class RegisterView(APIView):
    permission_classes = [AllowAny]  # Allows anyone to register
    authentication_classes = []  # No authentication required for registration

    @swagger_auto_schema(request_body=UserSerializer)  # Generate swagger docs for request body
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)