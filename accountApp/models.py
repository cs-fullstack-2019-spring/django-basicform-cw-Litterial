from django.db import models
from django.utils import timezone


# Create your models here.
class Account(models.Model):
    name = models.CharField(default="", max_length=200)
    checking = models.DecimalField(max_digits=16, decimal_places=4)
    savings = models.DecimalField(max_digits=16, decimal_places=4)
    dateTimeOpen = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'
