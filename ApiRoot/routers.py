from rest_framework import routers
from blog.viewsets import BlogViewSet

router = routers.SimpleRouter() # Simple default router for autogeneration of URLs for a DRF Viewset
router.register(r'blog', BlogViewSet, basename="blog") # Register the viewset to router; basename is for constructing URL names for ViewSet
 
urlpatters = router.urls # Set the URL patterns
