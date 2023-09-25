from django.db import models

# Create your models here.

class logindata(models.Model):
    email=models.EmailField(null=True)
    password=models.CharField(max_length=30,null=True)