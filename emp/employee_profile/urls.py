from django.urls import path
from .views import create_profile, profile_list

urlpatterns = [
    path('create_profile/', create_profile, name='create_profile'),
    path('profiles/', profile_list, name='profile_list'),

]
