from django.contrib import admin

# Register your models here.
from modelformsApp.models import Manager, Employee

class ManagerAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'department', 'modified_date']
    list_filter = ['age']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'salary', 'reporting_manager', 'modified_date']
    list_filter = ['age', 'salary']
    search_fields = ['name']
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'age')
        }),
        ('Designation', {
            'fields': ('salary', 'designation')
        }),
        ('Reporting Manager', {
            'fields': ('reporting_manager', )
        })
    )

admin.site.register(Manager, ManagerAdmin)
admin.site.register(Employee, EmployeeAdmin)