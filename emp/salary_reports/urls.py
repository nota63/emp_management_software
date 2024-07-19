from django.urls import path,include
from .views import generate_salary_reports,check_history

urlpatterns = [
    path("generate_salary_reports/", generate_salary_reports, name='generate_salary_reports'),
    path("check_history/",check_history, name='check_history'),
]
