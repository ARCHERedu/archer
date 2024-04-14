from django.db import models
from datetime import datetime

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=10000)
    email = models.EmailField(max_length=100000)
    password = models.CharField(max_length=100000)
    grade = models.CharField(max_length=1000)
    school = models.CharField(max_length=100000)
    state = models.CharField(max_length=100000) 
    city = models.CharField(max_length=100000) 
    country = models.CharField(max_length=100000) 
    date = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))

class Users(models.Model):
    name = models.CharField(max_length=10000)
    email = models.EmailField(max_length=100000)
    password = models.CharField(max_length=100000)
