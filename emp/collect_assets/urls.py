from django.urls import path,include
from .views import collect_assets,view_collected_assets,delete_collected_assets,download_assets_csv


urlpatterns = [
    path("collect_assets/",collect_assets, name='collect_assets'),
    path("view_collected_assets/",view_collected_assets,name='view_collected_assets'),
    path("delete_collected_assets/<int:asset_id>/",delete_collected_assets,name='delete_collected_assets'),
    path('download-assets/',download_assets_csv, name='download_assets_csv'),


]
