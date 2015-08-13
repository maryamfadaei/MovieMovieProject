from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from discussion.models import Topic, Topic_Form

# Create your views here.
def index(request):#the main page of app contact
    latest_topic_list = Topic.objects.all().order_by('title')#catch the newest list of contact
    context = {'latest_topic_list': latest_topic_list}
    return render(request, 'discussion/index.html', context)#context is optional, but it is needed to load contact list before loading template

def detail(request, topic_id):#load the detail of a contact, because url need a contact id, so in function need two var
    topic = get_object_or_404(Topic, pk=topic_id)#get the full data of a contact from database according the id
    return render(request, 'discussion/detail.html', {'topic': topic})#load the specific detail of the contact

def new(request):#load the template of creating a new contact
    return render(request, 'discussion/new.html')

def create_topic(request):#the action of posting the new contact to database. Should create a modelform in model.py.
    if request.method == 'POST':
        form=Topic_Form(request.POST)#create data to database
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            form.save(commit=True)#have to save, the data will be uploaded
            return index(request)#go back to the main page
    return index(request)

#def edit(request, topic_id):#load the page of editting the current contact
 #   topic = get_object_or_404(Topic, pk=topic_id)
  #  return render(request, 'discussion/edit.html', {'topic': topic})#load the page with current contact information

def update(request, topic_id):#post modified data to the current contact
    topic = get_object_or_404(Topic, pk=topic_id)
    if request.method == 'POST':
        form=Topic_Form(request.POST, instance=topic)#edit current contact data in database
        if form.is_valid():
            topic.title = form.cleaned_data['title']
            topic.text = form.cleaned_data['text']
            form.save(commit=True)
            return index(request)#go back to main page
    return index(request)
