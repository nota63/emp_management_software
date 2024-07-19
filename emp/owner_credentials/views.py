from django.shortcuts import render, redirect, get_object_or_404
from .models import OwnerCredentials
from .forms import OwnerForm
from django.contrib import messages


# Create your views here.

def update_credentials(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            admin_username = form.cleaned_data['admin_username']
            admin_password = form.cleaned_data['admin_password']
            web_username = form.cleaned_data['web_username']
            web_password = form.cleaned_data['web_password']
            updated_on = form.cleaned_data['updated_on']
            data = OwnerCredentials(admin_username=admin_username, admin_password=admin_password,
                                    web_username=web_username, web_password=web_password, updated_on=updated_on)
            data.save()
            messages.success(request, 'Credentials Updated  ')
            return redirect('update_credentials')
    else:
        form = OwnerForm()
    return render(request, 'owner_credentials/update_credentials.html', {'form': form})


def see_credentials(request):
    data = OwnerCredentials.objects.all()
    return render(request, 'owner_credentials/see_credentials.html', {'data': data})


def delete_owner_credentials(request, cred2_id):
    credential = get_object_or_404(OwnerCredentials, id=cred2_id)
    credential.delete()
    messages.success(request, 'Credentials deleted!')
    return redirect('see_credentials')
