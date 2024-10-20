from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import ProjectData
from django.db.models import Q

from home import models

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

def search_page(request):
    query = request.GET.get('query')
    
    if query:
        # Search for matching RoomType or FurnitureHighlights in ProjectData model
        projects = ProjectData.objects.filter(
            models.Q(RoomType__icontains=query) | models.Q(FurnitureHighlights__icontains=query)
        )
        if not projects:
            message = "Nothing matches your search criteria."
        else:
            message = None
    else:
        # Show 10 default projects if no search is performed
        projects = ProjectData.objects.all()[:10]
        message = None

    return render(request, 'search_page.html', {'projects': projects, 'message': message})
