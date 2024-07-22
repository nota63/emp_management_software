from django import forms
from django.contrib.auth.models import User

from .models import Cred


class CredForm(forms.Form):
    web_username = forms.CharField(max_length=100)
    web_password = forms.CharField(max_length=20)
    role = forms.CharField(max_length=50)
    role_password = forms.CharField(max_length=100)















