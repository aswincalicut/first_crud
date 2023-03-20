from django.db import models

# Create your models here.
class todo(models.Model):
    date = models.DateField()
    content = models.CharField(max_length=250)
    time = models.TimeField()

