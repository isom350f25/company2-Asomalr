from django.urls import path
from . import views

urlpatterns = [
    path('employeeslist/', views.employee_list, name='employee_list'),
]