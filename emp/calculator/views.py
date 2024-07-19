from django.shortcuts import render
from .forms import CalculatorForm

def calculate(expression):
    try:
        # Evaluate the expression safely
        result = eval(expression, {'__builtins__': None}, {})
    except Exception as e:
        result = str(e)
    return result

def calculator(request):
    form = CalculatorForm()
    result = None
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            expression = form.cleaned_data['expression']
            result = calculate(expression)
    return render(request, 'calculator/calculator.html', {'form': form, 'result': result})
