from django import forms

class commentForm(forms.Form):
    Comment = forms.CharField()