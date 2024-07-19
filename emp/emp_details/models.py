from django.db import models


# Create your models here.

class EmpDetails(models.Model):
    name = models.CharField(max_length=300)
    role = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    contact = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    joined = models.CharField(max_length=300)


    def __str__(self):
        return f"Employee details of {self.name}"