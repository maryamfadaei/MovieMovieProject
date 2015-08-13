from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import datetime
# Create your views here.
def index(request):#load the page of homepage
    return render(request, 'homepage/index.html')

def jump(request):#load the page of jump page
    return render(request, 'homepage/jump.html')

def dragon2(request):#load the page of dragon page
    return render(request, 'homepage/dragon2.html')
    
def tammy(request):#load the page of tammy page
    return render(request, 'homepage/tammy.html')

def dawn_of_the_planet_of_the_apes(request):#load the page of film detail page
    return render(request, 'homepage/dawn_of_the_planet_of_the_apes.html')
    
def transformers_age_of_extinction(request):#load the page of film detail page
    return render(request, 'homepage/transformers_age_of_extinction.html')

def rank(request):#get rank data from boxoffice.com
    rank_url = "http://www.boxoffice.com/statistics/bo_numbers/daily/"
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    rank_url = rank_url+current_date
    return HttpResponseRedirect(rank_url)