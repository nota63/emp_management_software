from django import forms


class CredentialsForm(forms.Form):
    web_username = forms.CharField(max_length=200, label='Web Username')
    web_password = forms.CharField(max_length=200, label='Web password')
    role = forms.CharField(max_length=200, label='Role')
    unique_key = forms.CharField(max_length=200, label='Unique Key')
