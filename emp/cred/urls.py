from django.urls import path,include
from .views import update_credentials,view_creds,delete_creds


urlpatterns = [

    path("user_update_credentials/",update_credentials,name='user_update_credentials'),
    path("view_creds/",view_creds,name='view_creds'),
    path("delete_creds/<int:cred_id>/",delete_creds,name='delete_creds'),

]