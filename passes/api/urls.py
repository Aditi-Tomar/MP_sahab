from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PassViewSet

app_name = 'passes_api'

router = DefaultRouter()
router.register(r'passes', PassViewSet, basename='pass')

urlpatterns = [
    path('', include(router.urls)),
] 