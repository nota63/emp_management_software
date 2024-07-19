from django import forms

class CalculatorForm(forms.Form):
    expression = forms.CharField(
        label='Expression',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter expression'})
    )
