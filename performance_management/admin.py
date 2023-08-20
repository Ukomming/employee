from django.contrib import admin
from .models import Goal, PerformanceReview ,Rating, DevelopmentPlan, Feedback

# Register your models here.
admin.site.register(Goal)
admin.site.register(PerformanceReview)
admin.site.register(Rating)
admin.site.register(DevelopmentPlan)
admin.site.register(Feedback)

