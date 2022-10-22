from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination


def say_hello(request):
    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests': dests})


def front(request):
    context = {}
    return render(request, "index.html", context)
