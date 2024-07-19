from django.urls import path,include
from .views import add_details,view_emp_details,delete_emp_details

urlpatterns = [
  path("add_details/",add_details,name='add_details'),
  path("view_emp_details/",view_emp_details,name='view_emp_details'),
  path("delete_emp_details/<int:employee_id>/",delete_emp_details,name='delete_emp_details'),

 ]