from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import pyttsx3
from .forms import PerformanceForm
from .models import Performance


# Create your views here.

def add_performance(request):
    if request.method == 'POST':
        form = PerformanceForm(request.POST)
        if form.is_valid():
            emp_name = form.cleaned_data['emp_name']
            emp_role = form.cleaned_data['emp_role']
            performance = form.cleaned_data['performance']
            date = form.cleaned_data['date']
            reward = form.cleaned_data['reward']
            suggestion = form.cleaned_data['suggestion']
            data = Performance(emp_name=emp_name, emp_role=emp_role, performance=performance, date=date, reward=reward,
                               suggestion=suggestion)
            data.save()
            messages.success(request, f'Employee {emp_name} performance updated!')
            engine = pyttsx3.init()
            engine.say(f'Performance Updated of {emp_name}')
            engine.runAndWait()

    else:
        form = PerformanceForm
    return render(request, 'performance/add_performance.html', {'form': form})


def view_performance(request):
    data = Performance.objects.all()
    return render(request, 'performance/view_performance.html', {'data': data})


