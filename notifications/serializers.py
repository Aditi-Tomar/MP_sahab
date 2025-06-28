from rest_framework import serializers
from .models import NotificationTemplate, NotificationType, NotificationLog

class NotificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationType
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

class NotificationTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationTemplate
        fields = ['id', 'name', 'notification_type', 'subject', 'content', 'template_id', 'created_at', 'updated_at']

class NotificationLogSerializer(serializers.ModelSerializer):
    template_name = serializers.CharField(source='template.name', read_only=True)
    
    class Meta:
        model = NotificationLog
        fields = ['id', 'recipient', 'template', 'template_name', 'channel', 'status', 'error_message', 'sent_at', 'created_at']
        read_only_fields = ['status', 'error_message', 'sent_at'] 