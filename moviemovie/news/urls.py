from django.conf.urls import patterns, url
from news import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),#the home page of news
    url(r'^reese_witherspoon/$', views.reese_witherspoon, name='reese_witherspoon'),
    url(r'^unbroken/$', views.unbroken, name='unbroken'),
    url(r'^galaxy/$', views.galaxy, name='galaxy'),
)
