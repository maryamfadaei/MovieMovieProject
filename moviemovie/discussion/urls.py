
from django.conf.urls import url

from discussion import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^(?P<topic_id>\d+)/$', views.detail, name='detail'),
    url(r'^new/create_topic/$', views.create_topic, name='Create Topic'),
	#url(r'^(?P<topic_id>\d+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<topic_id>\d+)/edit/finish/$', views.update, name='Update Topic')
]

