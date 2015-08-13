from django.db import models
from django.forms import ModelForm
from django.contrib import admin

# Create your models here.
class movie(models.Model):
    movie_name = models.CharField(max_length=500)
    release_date = models.DateField('Date Published', null=True, blank=True)
    duration = models.CharField(max_length=10, null=True, blank=True)
    genre = models.CharField(max_length=1500, null=True, blank=True)
    plot = models.CharField(max_length=10000, null=True, blank=True)
    director = models.CharField(max_length=500, null=True, blank=True)
    cast = models.CharField(max_length=500, null=True, blank=True)
    producer = models.CharField(max_length=500, null=True, blank=True)
    writer = models.CharField(max_length=500, null=True, blank=True)
    trailer = models.URLField(null=True, blank=True)
    gallery1 = models.ImageField(upload_to='/Users/lichengyu/Desktop/media/', null=True, blank=True)
    gallery2 = models.ImageField(upload_to='/Users/lichengyu/Desktop/media/', null=True, blank=True)
    gallery3 = models.ImageField(upload_to='/Users/lichengyu/Desktop/media/', null=True, blank=True)
    gallery4 = models.ImageField(upload_to='/Users/lichengyu/Desktop/media/', null=True, blank=True)

    def __unicode__(self):  
        return (self.movie_name)

class movie_form(ModelForm):#help to put data in a html form into database
    class Meta:
        model = movie
        fields = ['movie_name', 'release_date', 'duration', 'genre', 'plot', 'director', 'cast', 'producer', 'writer', 'trailer', 'gallery1', 'gallery2', 'gallery3', 'gallery4']

