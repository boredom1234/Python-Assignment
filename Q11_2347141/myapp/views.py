# myapp/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def register(request):
    return render(request, 'myapp/register.html')

def about(request):
    return render(request, 'myapp/about.html')
