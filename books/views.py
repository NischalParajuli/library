from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from accounts.permissions import IsAdmin
from .models import Book
from .serializer import BookSerializer
from .pagination import BookPagination
from django.shortcuts import render

# BookViewSet for CRUD operations on Book model
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    search_fields = ['title', 'author', 'genre']
    filterset_fields = ['author', 'genre', 'is_available']
    ordering_fields = ['title', 'author']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdmin()]
        return [IsAuthenticated()]   


def landing(request):
    return render(request,'landing.html')
    



