from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)

class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=50, blank=True)
    project = models.CharField(max_length=150, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
