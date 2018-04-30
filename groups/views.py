from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic.base import TemplateView

from django.views import View

from groups.models import Group


def all_groups(request):
    return HttpResponse(render(request, 'all_groups.html', {'groups': Group.objects.all()}))

def add_group(request):

    if request.method == 'GET':
        return HttpResponse(render(request, 'add-group.html'))
    elif request.method == 'POST':

        name = request.POST.get('name')
        start_date = request.POST.get('startDate')
        max_students = request.POST.get('maxStudents')

        group = Group()
        group.name = name
        group.start_date = start_date
        group.max_students = max_students
        group.save()

    return redirect('/groups/all')

class GetGroup(TemplateView):

    template_name = "get-group.html"

    def get_context_data(self, id, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['group'] = Group.objects.get(id=id)
        except Group.DoesNotExist:
            return context
        return context



from django.views.generic.list import ListView


# class GroupListView(ListView):
#
#     model = Group
#     template_name = 'all_groups.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


# class AddGroupView(View):
#     def get(self, request):
#         return HttpResponse(render(request, 'add-group.html'))
#
#     def post(self, request):
#         name = request.POST.get('name')
#         start_date = request.POST.get('startDate')
#         max_students = request.POST.get('maxStudents')
#
#         group = Group()
#         group.name = name
#         group.start_date = start_date
#         group.max_students = max_students
#         group.save()
#
#         return redirect('/groups/all')

