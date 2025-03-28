from django import forms
from django.contrib.auth import authenticate
from .models import User

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'email' )