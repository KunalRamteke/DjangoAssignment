from django import forms
from .models import Contacts

class PostForm(forms.Form):    
    FirstName = forms.CharField()
    LastName = forms.CharField()
    Email = forms.EmailField()
    MobileNo = forms.DecimalField()