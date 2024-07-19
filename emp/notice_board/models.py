from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Notice(models.Model):
    notice_title = models.TextField()
    notice_content = HTMLField()

    def __str__(self):
        return f"Notice {self.notice_title}"
