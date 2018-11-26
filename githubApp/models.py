from django.db import models
from django.utils import timezone

class gitUser(models.Model):
    name = models.CharField(max_length = 100,  unique=True)
    date_added = models.DateTimeField(default=timezone.now)
    weight = models.IntegerField()

class link(models.Model):
    source = models.CharField(max_length = 100)
    target  = models.CharField(max_length = 100)
