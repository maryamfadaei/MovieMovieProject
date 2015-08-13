from discussion.models import Topic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


def index(request):
    #latest_topic_list = Topic.objects.all().order_by('pub_date')[:100]
    latest_topic_list = Topic.objects.all().order_by('title')[:100]
    context = {'latest_topic_list': latest_topic_list}
    return render(request, 'discussion/index.html', context)

def detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    return render(request, 'discussion/detail.html', {'topic': topic})

def edit(request, topic_id):
    p = get_object_or_404(Topic, pk=topic_id)
    try:
        p.title = request.POST['title']
        #p.pub_date = request.POST['pub_date']
        p.text = request.POST['text']
    except (KeyError, Topic.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'discussion/detail.html', {
            'Topic': p,
            'error_message': "You did wrong inputs.",
        })
    else:
        p.save()
        return HttpResponseRedirect(reverse('discussion:index'))


def new_topic(request):
	return render(request, 'discussion/new_topic.html')
	
def add_new(request):
    p = Topic()
    try:
        p.title = request.POST['title']
        #p.pub_date = request.POST['pub_date']
        p.text = request.POST['text']
    except (KeyError, Topic.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'discussion/detail.html', {
            'Topic': p,
            'error_message': "You did wrong inputs.",
        })
    else:
        p.save()
        return HttpResponseRedirect(reverse('discussion:index'))


Z
