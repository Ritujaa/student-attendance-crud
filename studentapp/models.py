from django.db import models
# Create your models here.
class stud(models.Model):
    name=models.CharField(max_length=50)
    roll_no=models.CharField(max_length=20,default=1)
    email=models.CharField(max_length=40)
    attendance_date =models.DateField(default='2024-01-01')
    attendance_status=models.CharField(max_length=20 ,default='present') 
    branch=models.CharField(max_length=40, default='computer')
    year=models.CharField(max_length=20,default='first year')

class log(models.Model):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=40)