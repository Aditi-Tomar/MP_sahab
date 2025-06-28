from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EventListAPIView, EventDetailAPIView, UpcomingEventsAPIView, PastEventsAPIView,
    EventCategoryListAPIView, EventsByCategoryAPIView
)

app_name = 'events_api'

router = DefaultRouter()
# Register each view as a ViewSet or use as_view() for APIViews
# For now, we will use as_view() with path for each, as these are not ViewSets

urlpatterns = [
    path('events/', EventListAPIView.as_view(), name='event-list'),
    path('events/<slug:slug>/', EventDetailAPIView.as_view(), name='event-detail'),
    path('events/upcoming/', UpcomingEventsAPIView.as_view(), name='upcoming-events'),
    path('events/past/', PastEventsAPIView.as_view(), name='past-events'),
    path('categories/', EventCategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:category_id>/events/', EventsByCategoryAPIView.as_view(), name='category-events'),
] 