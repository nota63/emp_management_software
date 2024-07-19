from django.shortcuts import render, redirect
from .forms import StaffForm
from .models import Staff
from django.contrib import messages
import time
import datetime


def logged(request):
    return render(request, 'staff/logged.html')


def staff_login(request):
    staff_data = Staff.objects.all()
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            emp_role = form.cleaned_data['emp_role']
            emp_name = form.cleaned_data['emp_name']
            unique_key = form.cleaned_data['unique_key']
            staff_data = Staff(emp_role=emp_role, emp_name=emp_name, unique_key=unique_key)
            staff_data.save()
            if emp_role == 'manager' and unique_key == '8888':
                messages.success(request, "logged in as a manager")
                return redirect('logged')

            elif emp_role == 'developer' and unique_key == 'dg32dd':
                messages.success(request, 'logged in as a developer')
                return redirect('logged')

            elif emp_role == 'hr' and unique_key == '9999':
                messages.success(request, 'logged in as HR')
                return redirect('hr_page')

            elif emp_role == 'sales' and unique_key == 'det55w':
                messages.success(request, 'logged in as sales')
                return redirect('logged')

            elif emp_role == 'marketing' and unique_key == 'dte66w':
                messages.success(request, "logged in as marketing")
                return redirect('logged')

            elif emp_role == 'support' and unique_key == '3552gg':
                messages.success(request, "Logged in as support")
                return redirect('logged')

            elif emp_role == 'accountant' and unique_key == '35352':
                messages.success(request, 'logged in as an accountant')
                return redirect('logged')

            elif emp_role == 'admin' and unique_key == ' dhs66':
                messages.success(request, 'logged in as an admin')
                return redirect('logged')

            elif emp_role == 'it_support' and unique_key == 'dhy777':
                messages.success(request, "logged in as It support")
                return redirect('logged')

            elif emp_role == 'project_manager' and unique_key == '272521':
                messages.success(request, 'Logged in as a project manager')
                return redirect('logged')

            elif emp_role == 'designer' and unique_key == 'uyw55':
                messages.success(request, 'logged in as a designer')
                return redirect('logged')

            elif emp_role == 'product_manager' and unique_key == 'te5322':
                messages.success(request, "Logged in as a product_manager")
                return redirect('logged')

            elif emp_role == 'operations' and unique_key == 'tew33':
                messages.success(request, "logged in as operations ")
                return redirect('logged')

            elif emp_role == 'executive' and unique_key == 'eye772':
                messages.success(request, "logged in as an executive")
                return redirect('logged')

            elif emp_role == 'intern' and unique_key == '711552':
                messages.success(request, 'logged in as an intern')
                return redirect('logged')

            elif emp_role == 'cleaner' and unique_key == 'wy65111':
                messages.success(request, 'logged in as a cleaner')
                return redirect('logged')

            elif emp_role == 'security' and unique_key == '2544hww':
                messages.success(request, 'logged in as security')
                return redirect('logged')

            elif emp_role == 'piun' and unique_key == '1234':
                messages.success(request, 'logged in as piun')
                return redirect('logged')
    else:
        messages.error(request,'invalid credentials! may be you are not staff member')
        form = StaffForm()

    return render(request, 'staff/staff_login.html', {'form': form})


#  STAFF
def manager_login_view(request):
    manager_logins = Staff.objects.filter(emp_role='manager')
    return render(request, 'staff/manager_login_view.html', {'manager_logins': manager_logins})


def developer_login_view(request):
    developer_logins = Staff.objects.filter(emp_role='developer')
    return render(request, 'staff/developer_login_view.html', {'developer_logins': developer_logins})


def hr_login_view(request):
    hr_logins = Staff.objects.filter(emp_role='hr')
    return render(request, 'staff/hr_login_view.html', {'hr_logins': hr_logins})


def sales_login_view(request):
    sales_logins = Staff.objects.filter(emp_role='sales')
    return render(request, 'staff/sales_login_view.html', {'sales_logins': sales_logins})


def marketing_login_view(request):
    marketing_logins = Staff.objects.filter(emp_role='marketing')
    return render(request, 'staff/marketing_login_view.html', {'marketing_logins': marketing_logins})


def support_login_view(request):
    support_logins = Staff.objects.filter(emp_role='support')
    return render(request, 'staff/support_login_view.html', {'support_logins': support_logins})


def accountant_login_view(request):
    accountant_logins = Staff.objects.filter(emp_role='accountant')
    return render(request, 'staff/accountant_login_view.html', {'accountant_logins': accountant_logins})


def admin_login_view(request):
    admin_logins = Staff.objects.filter(emp_role='admin')
    return render(request, 'staff/admin_login_view.html', {'admin_logins': admin_logins})


def it_support_login_view(request):
    it_logins = Staff.objects.filter(emp_role='it_support')
    return render(request, 'staff/it_login_view.html', {'it_logins': it_logins})


def project_manager_view(request):
    project_manager_logins = Staff.objects.filter(emp_role='project_manager')
    return render(request, 'staff/project_manager_view.html', {'project_manager_logins': project_manager_logins})


def designer_login_view(request):
    designer_logins = Staff.objects.filter(emp_role='designer')
    return render(request, 'staff/designer_login_view.html', {'designer_logins': designer_logins})


def product_manager_view(request):
    product_manager_logins = Staff.objects.filter(emp_role='product_manager')
    return render(request, 'staff/product_manager_view.html', {'product_manager_logins': product_manager_logins})


def operations_login_view(request):
    operations_logins = Staff.objects.filter(emp_role='operations')
    return render(request, 'staff/operations_login_view.html', {'operations_logins': operations_logins})


def executive_login_view(request):
    executive_logins = Staff.objects.filter(emp_role='executive')
    return render(request, 'staff/executive_login_view.html', {'executive_logins': executive_logins})


def intern_login_view(request):
    intern_logins = Staff.objects.filter(emp_role='intern')
    return render(request, 'staff/intern_login_view.html', {'intern_logins': intern_logins})


def cleaner_login_view(request):
    cleaner_logins = Staff.objects.filter(emp_role='cleaner')
    return render(request, 'staff/cleaner_login_view.html', {'cleaner_logins': cleaner_logins})


def security_login_view(request):
    security_logins = Staff.objects.filter(emp_role='security')
    return render(request, 'staff/security_login_view.html', {'security_logins': security_logins})


def piun_login_view(request):
    piun_logins = Staff.objects.filter(emp_role='piun')
    return render(request, 'staff/piun_login_view.html', {'piun_logins': piun_logins})
