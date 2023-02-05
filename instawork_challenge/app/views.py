from django.shortcuts import render, redirect
from django.views import View
from .models import TeamMember, TeamMemberForm

class IndexView(View):
    template = 'index.html'

    def get(self, request):
        team_members = TeamMember.objects.all()
        print(team_members)
        return render(request, self.template, { 'team_members': team_members })

class AddView(View):
    template = 'add.html'
    def get(self, request):
        form = TeamMemberForm()
        return render(request, self.template, { 'form': form })

    def post(self, request):
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')

class EditView(View):
    template = 'add.html'
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

class DeleteView(View):
    def get(self, request, id):
        member = TeamMember.objects.get(id = id)
        member.delete()
        return redirect('index')