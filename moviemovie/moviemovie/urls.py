from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^homepage/', include('homepage.urls', namespace="homepage")),
    url(r'^news/', include('news.urls', namespace="news")),
    url(r'^payment/', include('payment.urls', namespace="payment")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^movie_signin/', include('movie_signin.urls', namespace="movie_signin")),
    url(r'^location/', include('location.urls', namespace="location")),
    url(r'^thirdauth/', include('thirdauth.urls', namespace='thirdauth')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^search/', include('search.urls', namespace="search")),
    url(r'^discussion/', include('discussion.urls', namespace="discussion")),
    url(r'^moviedatabase/', include('moviedatabase.urls', namespace="moviedatabase")),
    url(r'^comment/',include('commenting.urls',namespace = 'comment')),
)
