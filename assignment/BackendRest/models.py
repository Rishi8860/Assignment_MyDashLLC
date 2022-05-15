import email
from django.db import models
# Create your models here.   
class Data(models.Model):
    Username=models.CharField(max_length=15)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=64)
    Message=models.TextField(max_length=100,default="Nothing")
    created_at=models.DateTimeField(auto_now_add=True,blank=True)
    updated_at=models.DateTimeField(auto_now_add=True,blank=True)


