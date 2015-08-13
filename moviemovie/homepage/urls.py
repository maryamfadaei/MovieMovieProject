from django.conf.urls import patterns, url
from homepage import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),#the home page
    url(r'^jump/$', views.jump, name='jump'),#22 jump street
    url(r'^dragon2/$', views.dragon2, name='dragon2'),#how to train your dragon 2
    url(r'^tammy/$', views.tammy, name='tammy'),#tammy
    url(r'^dawn_of_the_planet_of_the_apes/$', views.dawn_of_the_planet_of_the_apes, name='dawn_of_the_planet_of_the_apes'),
    url(r'^transformers_age_of_extinction/$', views.transformers_age_of_extinction, name='transformers_age_of_extinction'),
    url(r'^rank$', views.rank, name='rank'),#add rank url
)