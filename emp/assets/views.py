from django.shortcuts import render, redirect, get_object_or_404
from .forms import AssestForm
from .models import Assets
from django.contrib import messages
import csv
from django.http import HttpResponse


# Create your views here.

def assets(request):
    asset = Assets.objects.all()
    if request.method == 'POST':
        form = AssestForm(request.POST)
        if form.is_valid():
            emp_name = form.cleaned_data['emp_name']
            emp_role = form.cleaned_data['emp_role']
            asset = form.cleaned_data['asset']
            date = form.cleaned_data['date']
            data = Assets(emp_name=emp_name, emp_role=emp_role, asset=asset, date=date)
            data.save()
            messages.success(request, 'Asset data added successfully')
            return redirect('assets')
    else:
        form = AssestForm()
    return render(request, 'assets/assets.html', {'form': form})


def view_asset_history(request):
    assets = Assets.objects.all()
    if request.method == 'GET':
        a_search = request.GET.get('a_search')
        if a_search != None:
            assets = Assets.objects.filter(emp_name__icontains=a_search)
    return render(request, 'assets/view_asset_history.html', {'assets': assets})


def delete_assets(request, asset_id):
    asset = get_object_or_404(Assets, id=asset_id)
    asset.delete()
    messages.success(request, 'Asset data deleted!')
    return redirect('view_asset_history')


def download_assets(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="assets.csv"'

    writer = csv.writer(response)
    writer.writerow(['Employee Name', 'Employee Role', 'Asset', 'Date'])

    assets = Assets.objects.all()
    for asset in assets:
        writer.writerow([asset.emp_name, asset.emp_role, asset.asset, asset.date])

    return response


