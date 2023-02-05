from django.shortcuts import redirect
from django.views import View
from ..models import TeamMember

class DeleteView(View):
    def get(self, request, id):
        member = TeamMember.objects.get(id = id)
        member.delete()
        return redirect('index')