from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeProfileForm
from .models import EmployeeProfile
from django.contrib import messages


def create_profile(request):
    if request.method == 'POST':
        form = EmployeeProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "profile has been created and stored to companies database!")
            return redirect('create_profile')
    else:
        form = EmployeeProfileForm()
    return render(request, 'employee_profile/create_profile.html', {'form': form})


def profile_list(request):
    profiles = EmployeeProfile.objects.all()
    return render(request, 'employee_profile/profile_list.html', {'profiles': profiles})
