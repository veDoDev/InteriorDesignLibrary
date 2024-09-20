from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import ProjectData

# Create your views here.

def home(request):
    return render(request,'index.html')

def contact(request):
    return render(request, 'contactus.html')

def about_us(request):
    return render(request, 'about_us.html')

# def page(request):
#     return render(request, 'page.html')

def page(request, pk):
    project = get_object_or_404(ProjectData, pk=pk)
    return render(request, 'page.html', {'project': project})
