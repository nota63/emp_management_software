from django import forms
from .models import EmployeeProfile

class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = ['first_name', 'last_name', 'email', 'job_title', 'department', 'contact_number', 'address', 'profile_picture']
