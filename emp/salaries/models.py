from django.db import models


# Create your models here.

class Salaries(models.Model):
    employee_name = models.CharField(max_length=200)
    employee_role = models.CharField(max_length=200)
    salary = models.TextField()

    def __str__(self):
        return f"Salary of {self.employee_role}"
