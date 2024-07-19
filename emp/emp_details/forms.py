from django import forms


class EmpForm(forms.Form):
    name = forms.CharField(max_length=300, label='name')
    role = forms.CharField(max_length=300, label='role')
    email = forms.CharField(max_length=300, label='email')
    contact = forms.CharField(max_length=300, label='contact')
    address = forms.CharField(max_length=300, label='address')
    joined = forms.CharField(max_length=300, label='joined date')
