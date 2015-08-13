from django.db import models
from django.db.models import *
from django.forms import ModelForm
# Create your models here.
class Movie(models.Model):
    title = CharField(max_length = 200)

class comment(models.Model):  
    movieId = models.IntegerField() # make this foreignKey to the movie table
    body = models.CharField(max_length=4000)
    parentId = models.IntegerField(null=True)
    author = models.CharField(max_length=50)
    created = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
    def __unicode__(self):
        return self.comment
class rate(models.Model):
    movieId = models.IntegerField() # make this foreignKey to the movie table
    rate = models.IntegerField()
    date = models.DateField()
    author = models.CharField(max_length=50)
  #  def __unicode__(self):
  #      return self.rate # replace with a definition for the numbers 
                           #maybe enum

class CommentForm(ModelForm):
    author = forms.CharField(required=False)
    class Meta:
        model = comment
        fields = ['body','author']