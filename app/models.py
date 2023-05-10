from django.db import models

# Create your models here.
class Sample(models.Model):
    Sid=models.IntegerField()
    Sname=models.CharField(max_length=100)
    Sage=models.IntegerField()
    Sstate=models.CharField(max_length=100)