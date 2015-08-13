from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from moviedatabase.models import movie, movie_form

# Create your views here.
def managemovie(request):
    return render(request, 'moviedatabase/index.html')

def add(request):
    return render(request, 'moviedatabase/success.html')

def detail(request, movie_id):
    movie_detail = get_object_or_404(movie, pk=movie_id)
    return render(request, 'moviedatabase/moviedetail.html', {'movie_detail':movie_detail})

