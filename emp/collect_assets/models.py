from django.db import models


# Create your models here.

class CollectAssets(models.Model):
    emp_name = models.CharField(max_length=200)
    emp_role = models.CharField(max_length=200)
    asset = models.CharField(max_length=400)
    condition = models.CharField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return f"Asset report from {self.emp_name}"
