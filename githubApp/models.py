from django.db import models
from django.utils import timezone

class gitUser(models.Model):
    name = models.CharField(max_length = 100)
    user_id = models.PositiveIntegerField(primary_key=True)
    date_added = models.DateTimeField(default=timezone.now)


class link(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    user_id = models.PositiveIntegerField()
    linkTo  = models.PositiveIntegerField()
