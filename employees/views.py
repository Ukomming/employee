from django.shortcuts import render
from .models import Employee

# Create your views here.


def employee_list(request):
    employees = Employee.objects.all()

    context = {'employees': employees}
    return render(request, 'employees/employee_list.html', context)

def employee_detail(request, slug):
    employee = Employee.objects.get(slug=slug)
    context={'employee': employee}
    print(employee.slug)
    return render(request, 'employees/employ_detail.html', context )