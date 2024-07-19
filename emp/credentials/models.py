from django.db import models


# Create your models here.

class Credentials(models.Model):
    web_username = models.CharField(max_length=200)
    web_password = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    unique_key = models.CharField(max_length=200)

    def __str__(self):
        return f"credentials of {self.role}"
