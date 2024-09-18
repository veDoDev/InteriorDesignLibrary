from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request,'index.html')

def contact(request):
    return render(request, 'contactus.html')