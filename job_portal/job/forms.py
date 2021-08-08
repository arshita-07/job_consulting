from django import forms
from .models import *
from django.forms import ModelForm 

class CV(ModelForm):
    class Meta:
        model = Application
        fields = ['cv']

class NewsLetter(forms.Form):
    email = forms.EmailField()


    