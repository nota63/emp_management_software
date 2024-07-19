from django.shortcuts import render, redirect, get_object_or_404
from .models import EmpDetails
from .forms import EmpForm
from django.contrib import messages


# Create your views here.


def add_details(request):
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            role = form.cleaned_data['role']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            address = form.cleaned_data['address']
            joined = form.cleaned_data['joined']
            data = EmpDetails(name=name, role=role, email=email, contact=contact, address=address, joined=joined)
            data.save()
            messages.success(request, 'Employee details added!')
            return redirect('add_details')
    else:
        form = EmpForm
    return render(request, 'details/add_details.html', {'form': form})


def view_emp_details(request):
    data = EmpDetails.objects.all()
    return render(request, 'details/view_emp_details.html', {'data': data})


def delete_emp_details(request, employee_id):
    employee = get_object_or_404(EmpDetails, id=employee_id)
    employee.delete()
    messages.success(request, 'Employee deleted')
    return redirect('view_emp_details')
