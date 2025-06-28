from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet

app_name = 'news_api'

router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')

urlpatterns = [
    path('', include(router.urls)),
] 