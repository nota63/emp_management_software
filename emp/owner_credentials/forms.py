from django import forms


class OwnerForm(forms.Form):
    admin_username = forms.CharField(max_length=200, label='Admin Username')
    admin_password = forms.CharField(max_length=200, label='Admin Password')
    web_username = forms.CharField(max_length=200, label='Web Username')
    web_password = forms.CharField(max_length=200, label='Web Password')
    updated_on=forms.CharField(max_length=200,label='Date')

