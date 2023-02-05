from django import forms
from .models import TeamMember

RADIO_CHOICES = [
    (0, "Regular - Can't delete members"),
    (1, "Admin - Can delete members")
]

class TeamMemberForm(forms.ModelForm):
    role = forms.ChoiceField(
        choices = RADIO_CHOICES,
        widget = forms.RadioSelect
    )
    class Meta:
        model = TeamMember
        fields = '__all__'