# Import APIView for custom API views
from rest_framework.views import APIView
# Import Response and status for API responses
from rest_framework.response import Response
from rest_framework import status, generics
# Import filters for search and filtering
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
# Import models
from borrow.models import BorrowRecord
from books.models import Book
# Import custom permissions
from accounts.permissions import IsMember, IsAdmin
# Import serializer
from .serializer import BorrowRecordSerializer
# Import pagination
from books.pagination import BorrowPagination
# Import timezone utilities
from django.utils.timezone import now
from datetime import timedelta

# View for borrowing a book
class BorrowBookView(APIView):
    permission_classes = [IsMember]

    def get(self, request):
        # Show all available books that can be borrowed
        available_books = Book.objects.filter(is_available=True)
        books_data = []
        for book in available_books:
            books_data.append({
                'id': book.id,
                'title': book.title,
                'author': book.author,
                'genre': book.genre,
                'book_no': book.book_no
            })
        return Response({
            'available_books': books_data,
            'total_available': len(books_data),
            'message': 'Use POST with book_id to borrow a book'
        })

    def post(self, request):
        user = request.user
        book_id = request.data.get('book_id')

        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

        if not book.is_available:
            return Response({'error': 'Book not available'}, status=status.HTTP_400_BAD_REQUEST)

        book.is_available = False
        book.save()

        borrow = BorrowRecord.objects.create(
            user=user,
            book=book,
            due_date=now().date() + timedelta(days=7)
        )

        return Response({"message": "Book borrowed successfully"}, status=status.HTTP_201_CREATED)


# View for returning a book
class ReturnBookView(APIView):
    permission_classes = [IsMember]

    def post(self, request):
        user = request.user
        book_id = request.data.get('book_id')

        try:
            borrow = BorrowRecord.objects.get(
                user=user,
                book_id=book_id,
                status='borrowed'
            )
        except BorrowRecord.DoesNotExist:
            return Response({'error': 'No active borrow record found'}, status=status.HTTP_404_NOT_FOUND)

        borrow.status = 'returned'
        borrow.return_date = now().date()
        borrow.save()

        # mark book available again
        borrow.book.is_available = True
        borrow.book.save()

        return Response({"message": "Book returned successfully"}, status=status.HTTP_200_OK)


# View for viewing borrow history
class BorrowHistoryView(generics.ListAPIView):
    serializer_class = BorrowRecordSerializer
    pagination_class = BorrowPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['status', 'due_date']
    search_fields = ['user__username', 'book__title']

    def get_permissions(self):
        return [IsAdmin()]

    def get_queryset(self):
        return BorrowRecord.objects.all().order_by('-borrow_date')