from django.urls import path
from . import views

urlpatterns = [
    path('employeeslist/', views.employee_list, name='employee_list'),
]



from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
]


