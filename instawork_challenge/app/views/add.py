from django.shortcuts import render, redirect
from django.views import View
from ..forms import TeamMemberForm

class AddView(View):
    template = 'add_edit.html'
    def get(self, request):
        form = TeamMemberForm()
        return render(request, self.template, { 'form': form })

    def post(self, request):
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')