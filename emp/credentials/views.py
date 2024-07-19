from django.shortcuts import render, redirect, get_object_or_404
from .models import Credentials
from .forms import CredentialsForm
from django.contrib import messages


# Create your views here.


def credentials(request):
    if request.method == 'POST':
        form = CredentialsForm(request.POST)
        if form.is_valid():
            web_username = form.cleaned_data['web_username']
            web_password = form.cleaned_data['web_password']
            role = form.cleaned_data['role']
            unique_key = form.cleaned_data['unique_key']
            cred = Credentials(web_username=web_username, web_password=web_password, role=role, unique_key=unique_key)
            cred.save()
            messages.success(request, 'Credentials Upgraded')
            return redirect('credentials')
    else:
        form = CredentialsForm
    return render(request, 'credentials/credentials.html', {'form': form})


def view_credentials(request):
    cred = Credentials.objects.all()
    return render(request, 'credentials/view_credentials.html', {'cred': cred})


def delete_credentials(request, cred_id):
    credentials = get_object_or_404(Credentials, id=cred_id)
    credentials.delete()
    messages.success(request, "Credentials deleted")
    return redirect('view_credentials')
