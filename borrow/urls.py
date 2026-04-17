# Import path for URL patterns
from django.urls import path
# Import views
from .views import BorrowBookView, ReturnBookView, BorrowHistoryView

# URL patterns for borrow app
urlpatterns = [
    path('borrow/', BorrowBookView.as_view(), name='borrow-book'),
    path('return/', ReturnBookView.as_view(), name='return-book'),
    path('history/', BorrowHistoryView.as_view(), name='borrow-history'),
]