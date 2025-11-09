from django.contrib import admin
from .models import Employee

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'date_joined', 'phone_number')
    search_fields = ('name', 'position')
    list_filter = ('position', 'date_joined')


from django.contrib import admin
from .models import Employee, Project

class ProjectInline(admin.TabularInline):
    model = Project.employees.through  # through table for ManyToMany
    extra = 1

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'date_joined', 'phone_number')
    search_fields = ('name', 'position')
    list_filter = ('position', 'date_joined')
    inlines = [ProjectInline]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'extra_pay')

    
