from rest_framework import serializers
from invitations.models import Person, Invitation, Assignment

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    person = PersonSerializer(read_only=True)
    person_id = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all(), source='person', write_only=True)
    class Meta:
        model = Assignment
        fields = ['id', 'invitation', 'person', 'person_id', 'is_gift_handler']

class InvitationSerializer(serializers.ModelSerializer):
    assignments = AssignmentSerializer(many=True, read_only=True)
    class Meta:
        model = Invitation
        fields = '__all__' 