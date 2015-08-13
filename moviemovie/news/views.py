from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def index(request):#load the page
    return render(request, 'news/index.html')

def galaxy(request):#load the page
    return render(request, 'news/galaxy.html')

def unbroken(request):#load the page 
    return render(request, 'news/unbroken.html')
    
def reese_witherspoon(request):#load the page
    return render(request, 'news/reese_witherspoon.html')
