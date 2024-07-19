from django.contrib import admin
from django.urls import path,include
from .views import assets,view_asset_history,delete_assets,download_assets


urlpatterns = [
      path("assets/", assets, name='assets'),
      path("view_asset_history/",view_asset_history, name='view_asset_history'),
      path("delete_assets/<int:asset_id>/",delete_assets, name='delete_assets'),
      path('download_assets/',download_assets, name='download_assets'),
]

