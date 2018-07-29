from django.db import models

# Create your models here.
class Quickstart(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.CharField(max_length=50)
    is_active = models.CharField(max_length=50, default='true')
    is_approved = models.CharField(max_length=50, default='false')