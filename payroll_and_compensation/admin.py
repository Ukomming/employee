from django.contrib import admin
from .models import Slary ,Bonus, Deduction,PayrollRun,PayStub,Taxform
# Register your models here.

admin.site.register(Slary)
admin.site.register(Bonus)
admin.site.register(Deduction)
admin.site.register(PayrollRun)
admin.site.register(PayStub)
admin.site.register(Taxform)

