from django import forms
from .models import CollectAssets


class AssetCollectionForm(forms.Form):
    emp_name = forms.CharField(max_length=200, label='Your Name')
    emp_role = forms.CharField(max_length=200, label='Your Role')
    asset = forms.CharField(max_length=400, label='Asset Name')
    condition = forms.CharField(max_length=500, label='Condition')
    date=forms.DateField(label='Date')

