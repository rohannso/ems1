from django.db import models
class Emp(models.Model):
    name=models.CharField(max_length=100)
    emp_id=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    department=models.CharField(max_length=50)
    working=models.BooleanField(default=True)
    address=models.CharField(max_length=200,default="adarsul")
    def __str__(self):
        return self.name

# Create your models here.
