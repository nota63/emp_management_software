from django.db import models


# Create your models here.

class Performance(models.Model):
    emp_name = models.CharField(max_length=200)
    emp_role = models.CharField(max_length=200)
    performance=models.CharField(max_length=200)
    date=models.DateField()
    reward=models.CharField(max_length=200)
    suggestion=models.CharField(max_length=200)

    def __str__(self):
        return f"performance report of {self.emp_name}"
