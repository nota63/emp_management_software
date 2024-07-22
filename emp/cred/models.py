from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Cred(models.Model):
    web_username = models.CharField(max_length=100)
    web_password = models.CharField(max_length=20)
    role = models.CharField(max_length=50)
    role_password = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"
