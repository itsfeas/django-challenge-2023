from django.shortcuts import render, redirect
from django.core.exceptions import BadRequest
from django.views import View
from ..models import TeamMember
from ..forms import TeamMemberForm

class EditView(View):
    template = 'add_edit.html'
    def get(self, request, id):
        member = TeamMember.objects.get(id = id)
        form = TeamMemberForm(instance=member)
        return render(request, self.template, { 'form': form, 'member_id': id })

    def post(self, request, id):
        member = TeamMember.objects.get(id = id)
        form = TeamMemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
        return redirect('index')