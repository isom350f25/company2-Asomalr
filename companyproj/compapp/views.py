from django.shortcuts import render
from .models import Employee

# Create your views here.

def employee_list(request):
    employees = Employee.objects.all().order_by('name')
    return render(request, 'employee_list.html', {'employees': employees})




def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    projects = projects.objects.all()
    return render(request, 'employee_detail.html', {'employee': employee, 'projects': projects})







