from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Avg

from students.models import Students
from groups.models import Group
from univ.models import Univ
from students.models import Attestat


# Create your views here.




def find_students(request):

    if request.method == 'GET':
        return HttpResponse(render(request, 'find_stud.html'))

    elif request.method == 'POST':

        name = request.POST.get('name')
        surname = request.POST.get('surname')
        find = Students.objects.get(name__icontains=f'{name}', surname__icontains=f'{surname}')
        return HttpResponse(render(request, 'find_stud.html', {'find': find}))

def all_stud(request):

    if request.method == 'GET':
        return HttpResponse(render(request, 'all_students.html', {'students': Students.objects.all()}))

    elif request.method == 'POST':
        ff = Students.objects.annotate(Avg('attestat__mark')).order_by('attestat__mark__avg')
        return HttpResponse(render(request, 'all_students.html', {'ff': ff}))

def add_stud(request):

    if request.method == 'GET':
        return HttpResponse(render(request, 'add_students.html', {'gr': Group.objects.all(),
                                                                  'un': Univ.objects.all()}))

    elif request.method == 'POST':

        name = request.POST.get('name')
        surname = request.POST.get('surname')
        group = request.POST.get('group')
        univ = request.POST.get('univ')


        stud = Students()
        stud.name = name
        stud.surname = surname
        stud.group_id = group
        stud.univ_id = univ
        stud.save()

    return redirect('/students/all')

def all_att(request):
    return HttpResponse(render(request, 'att_all.html', {'attestat' : Attestat.objects.all()}))

def attestat_add(request):

    if request.method == 'GET':
        return HttpResponse(render(request, 'att_add.html', {'students': Students.objects.all()}))

    elif request.method == 'POST':

        predmet = request.POST.get('name')
        mark = request.POST.get('surname')
        date = request.POST.get('date')
        student = request.POST.get('student')

        at = Attestat()
        at.predmet = predmet
        at.mark = mark
        at.date = date
        at.student_id = student
        at.save()

    return redirect('/students/attall')

