from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=50)
    phone=models.CharField( max_length=50)
    address=models.CharField(max_length=50)
    workig=models.BooleanField(default=True)
    department=models.CharField(max_length=50)