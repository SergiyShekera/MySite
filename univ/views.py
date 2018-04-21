from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

from univ.models import Univ

def add_univ(request):

    if request.method == 'GET':
        return HttpResponse(render(request, 'add_univ.html'))
    elif request.method == 'POST':

        name = request.POST.get('name')

        univ = Univ()
        univ.name = name
        univ.save()

    return redirect('/univ/add')