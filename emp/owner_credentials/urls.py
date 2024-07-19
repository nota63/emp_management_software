from django.urls import path,include
from .views import update_credentials,see_credentials,delete_owner_credentials

urlpatterns = [
   path("update_credentials/",update_credentials,name='update_credentials'),
   path("see_credentials/",see_credentials,name='see_credentials'),
   path("delete_owner_credentials/<int:cred2_id>/",delete_owner_credentials,name='delete_owner_credentials')
]