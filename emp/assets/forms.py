from django import forms
from .models import Assets


class AssestForm(forms.Form):
    emp_name = forms.CharField(max_length=200, label='Employee Name')
    emp_role = forms.CharField(max_length=200, label='Employee Role')
    asset = forms.CharField(max_length=200, label='Asset Name')
    date = forms.DateField()
