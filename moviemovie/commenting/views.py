# Create your views here.
from django.http import *
from django.core.context_processors import csrf
from commenting.models import comment,CommentForm
from django.shortcuts import *
from django.http import HttpResponse, HttpResponseRedirect


def hello(request):
    return HttpResponse("hello I am back")

def index(request):
    return render(request, 'index.html')
def comments(request,pk):
    comments = comment.objects.filter(movieId=pk).order_by("created")
    return render_to_response("comments.html" ,{'comments':comments})

def addcomment(request, pk):
    """Single post with comments and a comment form."""
    if request.method == 'POST' :
        c = CommentForm(request.POST)
        """add to refresh the page"""
        if c.is_valid():
          newComment = c.save(commit=False)
          if newComment.author == '' : 
            newComment.author = 'anonymous'
          newComment.movieId = pk
          newComment.save()
          comments = comment.objects.filter(movieId=pk).order_by("created")
    else:
            c=CommentForm()
    return render_to_response("index.html" ,{'comments':comments})

