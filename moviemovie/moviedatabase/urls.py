from django.conf.urls import patterns, url
from moviedatabase import views
urlpatterns = patterns('',
    #page of manage movie database
    url(r'^moviedatabase/$', views.managemovie, name='managemovie'),
    url(r'^moviedatabase/success/$', views.add, name='add'),
    url(r'^moviedtatbase/(?P<movie_id>\d+)/$', views.detail, name='detail'),
 )
