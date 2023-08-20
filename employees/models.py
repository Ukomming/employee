from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    slug =models.SlugField(unique=True, null=False)    

        
    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'
        ordering = ['last_name', 'first_name', ]

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(f'{self.last_name} {self.first_name}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("employees:employee_detail", kwargs={"slug": self.slug})
    
class EmployeeHistory(models.Model):
    Employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    job_title = models.CharField(max_length=100)
    company = models.CharField( max_length=100)
    description = models.TextField()
    

    class Meta:
        verbose_name = "employeehistory"
        verbose_name_plural = "employeehistoriess"

    def __str__(self):
        return f'{self.Employee.first_name} {self.start_date}'
    
class Skill(models.Model):
    """Model definition for Skill."""

    # TODO: Define fields here
    Employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    name = models.CharField( max_length=100)


    class Meta:
        """Meta definition for Skill."""

        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        """Unicode representation of Skill."""
        pass

class Qualification(models.Model):
    """Model definition for Qualification."""

    # TODO: Define fields here
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField( max_length=100)

    class Meta:
        verbose_name = 'Qualification'
        verbose_name_plural = 'Qualifications'

    def __str__(self):
        pass

class Certification(models.Model):
    """Model definition for Certification."""

    # TODO: Define fields here
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField( max_length=100)
    issuing_authority = models.CharField( max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    class Meta:
        verbose_name = 'Certification'
        verbose_name_plural = 'Certifications'

    def __str__(self):
        pass

class TrainingRecord(models.Model):
    """Model definition for TrainingRecord."""

    # TODO: Define fields here
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField( max_length=100)
    date = models.DateField()
    description = models.TextField()

class EmergencyContact(models.Model):
    """Model definition for EmergencyContact."""

    # TODO: Define fields here
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name= models.CharField( max_length=100)
    relationship = models.CharField( max_length=50)
    phone= models.CharField( max_length=15)
    email = models.EmailField()

    class Meta:
        verbose_name = 'EmergencyContact'
        verbose_name_plural = 'EmergencyContacts'

    def __str__(self):
        pass


    class Meta:
        verbose_name = 'TrainingRecord'
        verbose_name_plural = 'TrainingRecords'

    def __str__(self):
        pass





