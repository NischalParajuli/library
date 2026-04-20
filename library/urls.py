from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
# Import swagger view for API documentation
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from books.views import landing

schema_view = get_schema_view(
    openapi.Info(
        title="Library Management API",
        default_version='v1',
        description="API documentation for Library Management System",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[],
)

# Main URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin interface
    path('',landing,name = 'landing'),
    path('api/accounts/', include('accounts.urls')),  # User account endpoints
    path('api/books/', include('books.urls')),  # Book management endpoints
    path('api/borrow/', include('borrow.urls')),  # Borrowing endpoints

    path('api/login/', TokenObtainPairView.as_view(), name='login'),  # JWT login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh'),  # JWT token refresh

    # Swagger API documentation URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]
