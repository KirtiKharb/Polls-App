from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['emp_name']}),
        (None, {'fields' : ['emp_code']}),
        (None, {'fields' : ['salary']}),
        (None, {'fields' : ['password']}),
    ]
    list_display = ('id','emp_code' ,'emp_name', 'salary')
    list_filter = ['emp_code']
    list_order = ['-salary']
    search_fields = ['emp_code']

admin.site.register(Employee, EmployeeAdmin)


