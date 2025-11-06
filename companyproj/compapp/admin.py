from django.contrib import admin
from .models import Employee

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'date_joined', 'phone_number')
    search_fields = ('name', 'position')
    list_filter = ('position', 'date_joined')
