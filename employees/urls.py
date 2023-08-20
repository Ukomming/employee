from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.employee_list,name='employee_list'),
    path('<slug:slug>/', views.employee_detail,name='employee_detail'),

]