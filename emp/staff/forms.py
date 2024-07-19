from django import forms
from .models import Staff


class StaffForm(forms.ModelForm):
    class Meta():
        model=Staff
        fields=['emp_name','emp_role','unique_key']

