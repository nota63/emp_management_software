from django.urls import path,include
from .views import add_performance,view_performance


urlpatterns = [
    path('add_performance/',add_performance,name='add_performance'),
    path("view_performance/",view_performance,name='view_performance')

]