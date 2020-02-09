from django.shortcuts import render
from .models import Demoer

def demoers(request):
    demoers = Demoer.objects
    return render(request, 'demo/demoers.html', {'demoers': demoers})
