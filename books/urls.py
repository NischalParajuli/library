# Import DefaultRouter for automatic URL generation
from rest_framework.routers import DefaultRouter
# Import BookViewSet
from .views import BookViewSet

# Create router and register BookViewSet
router = DefaultRouter()
router.register('', BookViewSet)




# Use router URLs
urlpatterns = router.urls
