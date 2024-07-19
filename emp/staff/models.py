from django.db import models
from django.utils import timezone


# Create your models here.


class Staff(models.Model):
    ROLE_CHOICES = [
        ('manager', 'Manager'),
        ('developer', 'Developer'),
        ('hr', 'HR'),
        ('sales', 'Sales'),
        ('marketing', 'Marketing'),
        ('support', 'Support'),
        ('accountant', 'Accountant'),
        ('admin', 'Admin'),
        ('it_support', 'IT Support'),
        ('project_manager', 'Project Manager'),
        ('designer', 'Designer'),
        ('product_manager', 'Product Manager'),
        ('operations', 'Operations'),
        ('executive', 'Executive'),
        ('intern', 'Intern'),
        ('cleaner', 'Cleaner'),
        ('security', 'Security'),
        ('piun', 'Piun'),
    ]

    emp_name = models.CharField(max_length=200)
    emp_role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    unique_key = models.CharField(max_length=6)
    actual_time = actual_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.emp_name
