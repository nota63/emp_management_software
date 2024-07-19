import csv

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import CollectAssets
from .forms import AssetCollectionForm
from django.contrib import messages


# Create your views here.

def collect_assets(request):
    collect = CollectAssets.objects.all()
    if request.method == 'POST':
        form = AssetCollectionForm(request.POST)
        if form.is_valid():
            emp_name = form.cleaned_data['emp_name']
            emp_role = form.cleaned_data['emp_role']
            asset = form.cleaned_data['asset']
            condition = form.cleaned_data['condition']
            date = form.cleaned_data['date']
            collected_data = CollectAssets(emp_name=emp_name, emp_role=emp_role, asset=asset, condition=condition,
                                           date=date)
            collected_data.save()
            messages.success(request, "Asset data sent to company!")
            return redirect('collect_assets')
    else:
        form = AssetCollectionForm
    return render(request, 'collect_assets/collect_assets.html', {'form': form})


def view_collected_assets(request):
    assets = CollectAssets.objects.all()
    if request.method == 'GET':
        assets_search = request.GET.get('assets_search')
        if assets_search != None:
            assets = CollectAssets.objects.filter(emp_name__icontains=assets_search)
    return render(request, 'collect_assets/view_collected_assets.html', {'assets': assets})


def delete_collected_assets(request, asset_id):
    asset = get_object_or_404(CollectAssets, id=asset_id)
    asset.delete()
    messages.success(request, "Asset data deleted")
    return redirect('view_collected_assets')


def download_assets_csv(request):
    assets = CollectAssets.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="collected_assets.csv"'

    writer = csv.writer(response)
    writer.writerow(['Employee Name', 'Employee Role', 'Asset', 'Condition', 'Date Collected'])

    for asset in assets:
        writer.writerow([asset.emp_name, asset.emp_role, asset.asset, asset.condition, asset.date])

    return response
