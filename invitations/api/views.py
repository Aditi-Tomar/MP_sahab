from rest_framework import viewsets
from invitations.models import Person, Invitation, Assignment
from .serializers import PersonSerializer, InvitationSerializer, AssignmentSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    swagger_tags = ['Persons']

class InvitationViewSet(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    swagger_tags = ['Invitations']

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    swagger_tags = ['Assignments'] 