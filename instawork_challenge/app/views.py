from django.shortcuts import render
from django.views import View
from .models import TeamMember

class Index(View):
    template = 'index.html'

    def get(self, request):
        team_members = TeamMember.objects.all()
        return render(request, self.template, {'team_members': team_members})