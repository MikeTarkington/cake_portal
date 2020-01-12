from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def call_event(request):
    mrr = request.GET['mrr']
    date = request.GET['date']
    return render(request, 'call_event.html', {
        'mrr': mrr,
        'date': date
    })