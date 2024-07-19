from django import forms


class PerformanceForm(forms.Form):
    emp_name = forms.CharField(max_length=200,label='Employee Name')
    emp_role = forms.CharField(max_length=200,label='Employee Role')
    performance = forms.CharField(max_length=200,label='Performance')
    date=forms.DateField(label='Date')
    reward = forms.CharField(max_length=200,label='Reward')
    suggestion = forms.CharField(max_length=200,label='Suggestion')


