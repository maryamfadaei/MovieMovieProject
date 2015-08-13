from django.db import models
from django.forms import ModelForm


class Topic (models.Model):
	title = models.CharField(max_length=50)
	#pub_date = models.DateTimeField('date published')
	text = models.CharField(max_length=200)
	
	def __str__(self):              # __unicode__ on Python 2
		return self.title
		
		
		
		
class Topic_Form(ModelForm):#help to put data in a html form into database
    class Meta:
        model = Topic
        fields = ['title','text']
	
	#TODO: reference to user ID
	#author_id = models.ForeignKey(USR_ID)
    
#class Participant_Text (models.Model):
 #   topic = models.ForeignKey(Topic)
  #  text = models.CharField(max_length=500)
    
    #TODO: reference to user ID
	#author_id = models.ForeignKey(USR_ID)
