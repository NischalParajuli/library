# Import PageNumberPagination for paginating API responses
from rest_framework.pagination import PageNumberPagination

# Pagination class for Book list views
class BookPagination(PageNumberPagination):
    page_size = 10  # Default number of items per page
    page_size_query_param = 'page_size'  # Allow clients to set page size via query param
    max_page_size = 50  # Maximum allowed page size

# Pagination class for Borrow history views
class BorrowPagination(PageNumberPagination):
    page_size = 5  # Default number of items per page
    page_size_query_param = 'page_size'  # Allow clients to set page size via query param
    max_page_size = 20  # Maximum allowed page size