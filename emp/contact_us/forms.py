from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=300,label='Name')
    email = forms.CharField(max_length=300,label='Email')
    contact = forms.CharField(max_length=300,label='Contact')
    message = forms.CharField(max_length=300,label='Message')
    date = forms.DateField()
