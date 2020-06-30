from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    template = 'homepage.html'
    return render(request, template)

def about(request):
    return render(request, 'about.html')
