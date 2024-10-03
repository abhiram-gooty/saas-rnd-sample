from django.db import models

# Create your models here.

class pageVisit(models.Model):
    path = models.TextField(null=True,blank=True)
    timestamp = models.TimeField(auto_now_add=True)