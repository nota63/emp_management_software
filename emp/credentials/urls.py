from django.urls import path,include
from .views import credentials,view_credentials,delete_credentials

urlpatterns = [
    path("credentials/",credentials,name='credentials'),
    path("view_credentials/",view_credentials,name='view_credentials'),
    path("delete_credentials/<int:cred_id>/",delete_credentials,name='delete_credentials'),
]
