from django.db import models
from employees.models import Employee

# Create your models here.

class Shift(models.Model):
    """Model definition for Shift."""
    # TODO: Define fields here
    name =models.CharField( max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        verbose_name = 'Shift'
        verbose_name_plural = 'Shifts'

    def __str__(self):
        pass

class WorkDay(models.Model):
    """Model definition for WorkDay."""

    # TODO: Define fields here
    employee = models.ForeignKey(Employee,  on_delete=models.CASCADE)
    date = models.DateField()
    Shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
 
    class Meta:
        verbose_name = 'WorkDay'
        verbose_name_plural = 'WorkDays'

    def __str__(self):
        pass

class Attendance(models.Model):
    """Model definition for Attendance."""

    # TODO: Define fields here
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    is_present =models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'

    def __str__(self):
        pass

class TimeOffRequest(models.Model):
    """Model definition for TimeOffRequest."""

    # TODO: Define fields here
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    is_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'TimeOffRequest'
        verbose_name_plural = 'TimeOffRequests'

    def __str__(self):
        pass

class Timesheet(models.Model):
    """Model definition for Timesheet."""

    # TODO: Define fields here
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DecimalField(max_digits=5, decimal_places=2)
    class Meta:
        verbose_name = 'Timesheet'
        verbose_name_plural = 'Timesheets'

    def __str__(self):
        pass

class Report(models.Model):
    """Model definition for Report."""

    # TODO: Define fields here
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField( auto_now_add=True)

    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'

    def __str__(self):
        pass
