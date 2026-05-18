from django.db import models

# Create your models here.

class Employee(models.Model):
    empid = models.IntegerField()
    name= models.CharField(max_length=100)
    deptname = models.CharField(max_length=100)
    salary = models.IntegerField()
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to="users",null=True,blank=True)