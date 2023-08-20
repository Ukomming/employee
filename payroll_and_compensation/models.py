from django.db import models
from employees.models import Employee

# Create your models here.

class Slary(models.Model):
    """Model definition for Slary."""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount =models.DecimalField(max_digits=10, decimal_places=2)
    effective_date = models.DateField()

    # TODO: Define fields here

    class Meta:
        verbose_name = 'Slary'
        verbose_name_plural = 'Slarys'

    def __str__(self):
        pass


class Bonus(models.Model):
    """Model definition for Bonus."""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.CharField( max_length=100)
    date = models.DateField()
    # TODO: Define fields here

    class Meta:
        verbose_name = 'Bonus'
        verbose_name_plural = 'Bonuss'

    def __str__(self):
        pass


class Deduction(models.Model):
    """Model definition for Deduction."""

    # TODO: Define fields here
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.CharField( max_length=100)
    date = models.DateField()

    class Meta:
        verbose_name = 'Deduction'
        verbose_name_plural = 'Deductions'

    def __str__(self):
        pass


class PayrollRun(models.Model):
    """Model definition for PayrollRun."""

    # TODO: Define fields here
    Start_date = models.DateField()
    end_date = models.DateField()
    is_processed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'PayrollRun'
        verbose_name_plural = 'PayrollRuns'

    def __str__(self):
        pass

class PayStub(models.Model):
    """Model definition for PayStub."""

    # TODO: Define fields here
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Payroll_run = models.ForeignKey(PayrollRun, on_delete=models.CASCADE)
    pay_date = models.DateField()
    base_slary = models.DecimalField(max_digits=10, decimal_places=2)
    total_bonus = models.DecimalField(max_digits=10, decimal_places=2)
    total_deduction = models.DecimalField(max_digits=10, decimal_places=2)
    net_pay = models.DecimalField( max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'PayStub'
        verbose_name_plural = 'PayStubs'

    def __str__(self):
        pass


class Taxform(models.Model):
    """Model definition for Taxform."""

    # TODO: Define fields here
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    form_type =models.CharField( max_length=20)
    content = models.TextField()

    class Meta:
        verbose_name = 'Taxform'
        verbose_name_plural = 'Taxforms'

    def __str__(self):
        pass
