from django.db import models

class EmployeeProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
