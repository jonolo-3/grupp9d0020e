from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GraphDataPoints(models.Model):
    user = models.ForeignKey(User, unique=True)
    yVal = models.IntegerField()
