"""
URL configuration for emp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.context_processors import static
from django.urls import path,include
from emp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path("home",views.home,name='home'),
    path("generate_salary_reports/",include('salary_reports.urls')),
    path("staff_login/",include('staff.urls')),
    path("owner_login/",views.owner_login,name='owner_login'),
    path("owner_dashboard/",views.owner_dashboard,name='owner_dashboard'),
    path("employee_attendance/",views.employee_attendance,name='employee_attendance'),
    path("employee_salaries/",views.employee_salaries,name='employee_salaries'),
    path("notice_board/",views.notice_board,name='notice_board'),
    path("get_leaves/", views.get_leaves, name='get_leaves'),
    path("view_leaves/",views.view_leaves,name='view_leaves'),
    path('delete_leave/<int:leave_id>/', views.delete_leave, name='delete_leave'),
    path("assets/",include('assets.urls')),
    path("collect_assets/",include('collect_assets.urls')),
    path("create_profile/", include('employee_profile.urls')),
    path("calculator/",include('calculator.urls')),
    path("update_credentials/",include('owner_credentials.urls')),
    path("add_performance/",include('performance.urls')),
    path('create_id_card/', views.create_and_view_id_card, name='create_and_view_id_card'),
    path("hr_page/",views.hr_page,name='hr_page'),
    path("add_details/",include('emp_details.urls')),
    path("contact_us/",include('contact_us.urls')),
    path("coming_soon/",views.coming_soon,name='coming_soon'),
    path("update_credentials/",include('cred.urls'))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)