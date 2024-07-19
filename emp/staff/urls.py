from django.contrib import admin
from django.urls import path,include
from .views import staff_login, manager_login_view, developer_login_view, hr_login_view,logged, sales_login_view,marketing_login_view,support_login_view,accountant_login_view,admin_login_view, it_support_login_view,project_manager_view, designer_login_view, product_manager_view, operations_login_view, executive_login_view,intern_login_view,cleaner_login_view, security_login_view,piun_login_view


urlpatterns = [
   path('staff_login/', staff_login, name='staff_login'),
   path("manager_login_view/",manager_login_view,name='manager_login_view'),
   path("developer_login_view/", developer_login_view, name='developer_login_view'),
   path("hr_login_view/", hr_login_view, name='hr_login_view'),
   path("logged/", logged, name='logged'),
   path("sales_login_view/", sales_login_view, name='sales_login_view'),
   path("marketing_login_view/", marketing_login_view, name='marketing_login_view'),
   path("support_login_view/", support_login_view, name='support_login_view'),
   path("accountant_login_view/", accountant_login_view, name='accountant_login_view'),
   path("admin_login_view/", admin_login_view, name='admin_login_view'),
   path("it_support_login_view/", it_support_login_view, name='it_support_login_view'),
   path("project_manager_view/", project_manager_view, name='project_manager_view'),
   path("designer_login_view/", designer_login_view, name='designer_login_view'),
   path("product_manager_view/",product_manager_view, name='product_manager_view'),
   path("operations_login_view/", operations_login_view, name='operations_login_view'),
   path('executive_login_view/',executive_login_view, name='executive_login_view'),
   path("intern_login_view/",intern_login_view,name='intern_login_view'),
   path('cleaner_login_view/', cleaner_login_view, name='cleaner_login_view'),
   path("security_login_view/", security_login_view, name='security_login_view'),
   path("piun_login_view/", piun_login_view, name='piun_login_view')

]
