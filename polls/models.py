import datetime

from django.db import models
from django.utils import timezone

class Cat(models.Model):
    cat_name = models.CharField(max_length=256)
    