from django.db import models


# Create your models here.

class OwnerCredentials(models.Model):
    admin_username = models.CharField(max_length=200)
    admin_password = models.CharField(max_length=200)
    web_username = models.CharField(max_length=200)
    web_password = models.CharField(max_length=200)
    updated_on=models.CharField(max_length=200)

    def __str__(self):
        return f"Credentials of {self.admin_username} and {self.web_username}"
