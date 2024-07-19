from django.db import models


# Create your models here.
class Assets(models.Model):
    emp_name = models.CharField(max_length=200)
    emp_role = models.CharField(max_length=200)
    asset = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"Asset of {self.emp_name}"
