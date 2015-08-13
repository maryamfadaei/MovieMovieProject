from django.shortcuts import render

# Create your views here.
def search(request):#load the page of cart
    return render(request, 'search/search.html')
