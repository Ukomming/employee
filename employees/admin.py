from django.contrib import admin
from .models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug': ('last_name', 'first_name')} 