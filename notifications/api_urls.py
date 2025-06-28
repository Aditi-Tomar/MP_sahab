from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import NotificationTemplateViewSet, NotificationTypeViewSet, NotificationLogViewSet

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'templates', NotificationTemplateViewSet)
router.register(r'types', NotificationTypeViewSet)
router.register(r'logs', NotificationLogViewSet)

# The API URLs are determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
] 