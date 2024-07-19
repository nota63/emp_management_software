from django import forms
from .models import Salary


class Salary_Form(forms.ModelForm):
    class Meta():
        model = Salary
        fields = ['emp_name', 'emp_role', 'salary_credited', 'payment_method', 'date']
