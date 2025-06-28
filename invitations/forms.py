from django import forms
from django.forms.models import BaseInlineFormSet
from .models import Invitation, Person, Assignment
from voters.models import Voter

class InvitationForm(forms.ModelForm):
    mandal = forms.ChoiceField(
        choices=[('', "Select Mandal")] + sorted([
            (m, m) for m in set(Voter.objects.values_list('data__MANDAL', flat=True)) if m is not None and m != ''
        ]),
        required=False,
        widget=forms.Select(attrs={'class': 'styled-select'})
    )
    class Meta:
        model = Invitation
        fields = ['name', 'mobile_number', 'mandal', 'address_venue', 'area', 'file_upload']

class PersonForm(forms.ModelForm):
    assembly = forms.ChoiceField(
        choices=[('', "Select Assembly")] + sorted([
            (a, a) for a in set(Voter.objects.values_list('data__ASSEMBLY', flat=True)) if a is not None and a != ''
        ]),
        required=False,
        widget=forms.Select(attrs={'class': 'styled-select'})
    )
    mandal = forms.ChoiceField(
        choices=[('', "Select Mandal")] + sorted([
            (m, m) for m in set(Voter.objects.values_list('data__MANDAL', flat=True)) if m is not None and m != ''
        ]),
        required=False,
        widget=forms.Select(attrs={'class': 'styled-select'})
    )
    class Meta:
        model = Person
        fields = ['name', 'phone_number', 'email', 'address', 'assembly', 'mandal', 'area']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['person', 'is_gift_handler']

class BaseAssignmentFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        # Add any custom formset cleaning here if needed
        pass 