from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    ratings = models.IntegerField()