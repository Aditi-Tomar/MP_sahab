from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet, InvitationViewSet, AssignmentViewSet

app_name = 'invitations_api'

router = DefaultRouter()
router.register(r'persons', PersonViewSet, basename='person')
router.register(r'invitations', InvitationViewSet, basename='invitation')
router.register(r'assignments', AssignmentViewSet, basename='assignment')

urlpatterns = [
    path('', include(router.urls)),
] 