from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from django.utils import timezone

from .forms import CredForm
from .models import Cred
from django.contrib import messages


# Create your views here.

@login_required
def update_credentials(request):
    if request.method == 'POST':
        form = CredForm(request.POST)
        if form.is_valid():
            web_username = form.cleaned_data['web_username']
            web_password = form.cleaned_data['web_password']
            role = form.cleaned_data['role']
            role_password = form.cleaned_data['role_password']
            cred = Cred(user=request.user, web_username=web_username, web_password=web_password, role=role,
                        role_password=role_password)
            cred.save()
            messages.success(request, 'Credentials Updated successfully')
            return redirect('user_update_credentials')
    else:
        form=CredForm()
    return render(request, 'cred/update_credentials.html',{'form':form})


def view_creds(request):
    data=Cred.objects.filter(user=request.user)
    return render(request,'cred/view_creds.html',{'data':data})


def delete_creds(request,cred_id):
    credentials=get_object_or_404(Cred, id=cred_id)
    credentials.delete()
    messages.success(request,'credentials has been deleted')
    return redirect('view_creds')
