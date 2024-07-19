from django.db import models


# Create your models here.
class Salary(models.Model):
    emp_name = models.CharField(max_length=200)
    emp_role = models.CharField(max_length=200)
    salary_credited =models.CharField(max_length=200)
    payment_method = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"salary report of {self.emp_name}"


