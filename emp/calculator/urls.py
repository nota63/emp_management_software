from django.urls import path
from .views import calculator

urlpatterns = [
    path('calculator', calculator, name='calculator'),
]
