from django.db import models
from django.utils import timezone
# Create your models here.
class employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=150)
    mobile=models.CharField(max_length=10)
    dob=models.DateField(null=True,blank=True)
    Gender=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    country=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name and self.mobile
