from django.db import models
from django.forms import ModelForm


class Roles(models.IntegerChoices):
    REGULAR = 0, 'Regular'
    ADMIN = 1, 'Admin'

class TeamMember(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    role = models.PositiveIntegerField(default=Roles.REGULAR, choices=Roles.choices)

class TeamMemberForm(ModelForm):
    class Meta:
        model = TeamMember
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'role']