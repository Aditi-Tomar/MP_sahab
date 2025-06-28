from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import NotificationTemplate, NotificationType, NotificationLog
from .serializers import NotificationTemplateSerializer, NotificationTypeSerializer, NotificationLogSerializer
from .utils import NotificationSender

class NotificationTemplateViewSet(viewsets.ModelViewSet):
    queryset = NotificationTemplate.objects.all()
    serializer_class = NotificationTemplateSerializer

class NotificationTypeViewSet(viewsets.ModelViewSet):
    queryset = NotificationType.objects.all()
    serializer_class = NotificationTypeSerializer

class NotificationLogViewSet(viewsets.ModelViewSet):
    queryset = NotificationLog.objects.all()
    serializer_class = NotificationLogSerializer

    @action(detail=False, methods=['post'])
    def send(self, request):
        """Send a notification"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            notification_log = serializer.save()
            sender = NotificationSender()
            success, error = sender.send_notification(notification_log)
            
            if success:
                return Response({'status': 'sent'})
            return Response({'status': 'failed', 'error': error}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset.order_by('-created_at') 