from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    contact=models.CharField(max_length=300)
    message=models.CharField(max_length=300)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Contact request from {self.name}"


