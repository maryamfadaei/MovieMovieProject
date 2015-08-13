from django.conf.urls import patterns, url
from location import views
urlpatterns = patterns('',
    url(r'^$', views.location, name='location'),                      
)
