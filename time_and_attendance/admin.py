from django.contrib import admin
from .models import Shift , WorkDay,Attendance ,TimeOffRequest ,Timesheet,Report
# Register your models here.

admin.site.register(Shift)
admin.site.register(WorkDay)
admin.site.register(Attendance)
admin.site.register(TimeOffRequest)
admin.site.register(Timesheet)
admin.site.register(Report)              