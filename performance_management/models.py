from django.db import models
from employees.models import Employee
# Create your models here.


class Goal(models.Model):
    """Model definition for Goal."""
    # TODO: Define fields here
    employee =models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description =models.TextField()
    due_date = models.DateField()


    class Meta:
        verbose_name = 'Goal'
        verbose_name_plural = 'Goals'

    def __str__(self):
        pass

class PerformanceReview(models.Model):
    """Model definition for Review."""

    # TODO: Define fields here
    employee =models.ForeignKey(Employee, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='reviews_given')
    date = models.DateField()
    comments = models.DateField()

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        pass

class Rating(models.Model):
    """Model definition for Rating."""

    # TODO: Define fields here
    review = models.ForeignKey(PerformanceReview, on_delete=models.CASCADE)
    category = models.CharField( max_length=50)
    score = models.DecimalField( max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'

    def __str__(self):
        pass


class DevelopmentPlan(models.Model):
    """Model definition for DevelopmentPlan."""

    # TODO: Define fields here
    employee =models.ForeignKey(Employee, on_delete=models.CASCADE)
    goal = models.TextField()
    Training_needs = models.TextField()

    class Meta:
        verbose_name = 'DevelopmentPlan'
        verbose_name_plural = 'DevelopmentPlans'

    def __str__(self):
        pass


class Feedback(models.Model):
    """Model definition for Feedback."""

    # TODO: Define fields here
    employee =models.ForeignKey(Employee, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Employee,  on_delete=models.CASCADE, related_name='Feedback_given')
    date =  models.DateField()
    comment = models.TextField()

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        pass