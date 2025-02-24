from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Chutti(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=4000)
    days = models.CharField(max_length=200)
    date = models.DateField()
    from_date = models.DateField()
    to_date = models.DateField()
    status = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Leave application from {self.name}"
