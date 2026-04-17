# Import path for URL patterns
from django.urls import path
# Import RegisterView
from .views import RegisterView

# URL patterns for accounts app
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]
