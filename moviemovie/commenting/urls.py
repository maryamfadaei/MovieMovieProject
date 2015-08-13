from django.conf.urls import patterns, include, url
from commenting.views import *
from django.conf import settings
from commenting import views


urlpatterns = patterns('',   
    url(r'^$', views.index, name='index'),
    url(r'^index/$',index),
    url(r"^addcomment/(\d+)/$", addcomment),
    url(r'^comments/(\d+)/$',comments),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

 
)


