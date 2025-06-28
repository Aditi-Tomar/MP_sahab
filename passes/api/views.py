from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from passes.models import Pass
from django.utils import timezone
from .serializers import PassSerializer

class PassViewSet(viewsets.ModelViewSet):
    serializer_class = PassSerializer
    permission_classes = []

    def get_queryset(self):
        status_filter = self.request.query_params.get('status', 'PENDING')
        return Pass.objects.filter(status=status_filter).order_by('-created_at')

    @action(detail=False, methods=['get'])
    def pending(self, request):
        passes = Pass.objects.filter(status='PENDING').order_by('-created_at')
        serializer = self.get_serializer(passes, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def approved(self, request):
        passes = Pass.objects.filter(status='APPROVED').order_by('-processed_at')
        serializer = self.get_serializer(passes, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def rejected(self, request):
        passes = Pass.objects.filter(status='REJECTED').order_by('-processed_at')
        serializer = self.get_serializer(passes, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        pass_obj = self.get_object()
        if pass_obj.status != 'PENDING':
            return Response(
                {'error': 'This pass is not pending'},
                status=status.HTTP_400_BAD_REQUEST
            )
        pass_obj.status = 'APPROVED'
        pass_obj.processed_at = timezone.now()
        pass_obj.processed_by = request.user if request.user.is_authenticated else None
        pass_obj.save()
        serializer = self.get_serializer(pass_obj)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        pass_obj = self.get_object()
        if pass_obj.status != 'PENDING':
            return Response(
                {'error': 'This pass is not pending'},
                status=status.HTTP_400_BAD_REQUEST
            )
        pass_obj.status = 'REJECTED'
        pass_obj.processed_at = timezone.now()
        pass_obj.processed_by = request.user if request.user.is_authenticated else None
        pass_obj.save()
        serializer = self.get_serializer(pass_obj)
        return Response(serializer.data) 