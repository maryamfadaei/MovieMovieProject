from django.db import models
from django.forms import ModelForm
from django.contrib import admin
from django import forms
import datetime
# Create your models here.
class stock(models.Model):
    item_id = models.CharField(max_length=10)
    item_name = models.CharField(max_length=200)
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    provider_id = models.CharField(max_length=10, null=True, blank=True)
    def __unicode__(self):  
        return (self.item_id, self.item_name, self.quantity)

class stock_form(ModelForm):#help to put data in a html form into database
    class Meta:
        model = stock
        fields = ['item_id', 'item_name', 'price', 'quantity', 'provider_id']

class payment_info(models.Model):
    transaction_id = models.CharField(max_length=500, null=True, blank=True)
    user_id = models.CharField(max_length=50)
    item_id = models.CharField(max_length=10)
    transaction_date = models.DateTimeField('purchased date', null=True, blank=True)
    quantity = models.SmallIntegerField()
    total_price = models.CharField(max_length=50, null=True, blank=True)
    notes = models.CharField(max_length=1000, null=True, blank=True)
    def __unicode__(self):  
        return (self.transaction_id, self.user_id, self.item_id, self.transaction_date)

class payment_info_form(ModelForm):#help to put data in a html form into database
    class Meta:
        model = payment_info
        fields = ['transaction_id', 'user_id', 'item_id', 'transaction_date', 'quantity', 'total_price', 'notes']

class shipping(models.Model):
    transaction_id = models.CharField(max_length=500)
    shipping_address = models.CharField(max_length=500)
    def __unicode__(self):  
        return (self.transaction_id, self.shipping_address)

class shipping_form(ModelForm):#help to put data in a html form into database
    class Meta:
        model = shipping
        fields = ['transaction_id', 'shipping_address']

class payment_detailForm(forms.Form):
    firstname = forms.CharField(max_length=50, required=False)
    lastname = forms.CharField(max_length=50, required=False)
    company = forms.CharField(max_length=50, required=False)
    address1 = forms.CharField(max_length=50, required=False)
    address2 = forms.CharField(max_length=50, required=False)
    city = forms.CharField(max_length=50, required=False)
    state = forms.CharField(max_length=50, required=False)
    zipcode = forms.CharField(max_length=50, required=False)
    country = forms.CharField(max_length=50, required=False)
    phone = forms.CharField(max_length=50, required=False)
    cardtype = forms.CharField(max_length=50, required=False)
    cardnumber = forms.CharField(max_length=50, required=False)
    expire_month = forms.CharField(max_length=50, required=False)
    expire_year = forms.CharField(max_length=50, required=False)
    cvv2 = forms.CharField(max_length=50, required=False)
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    contactEmail = forms.EmailField(required=False)
    notes = forms.CharField(max_length=200, required=False)
    




