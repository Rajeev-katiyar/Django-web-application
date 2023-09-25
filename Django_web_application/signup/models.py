from django.db import models

# Create your models here.
class signdata(models.Model):
    user_name=models.CharField(max_length=50,null=True)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=20,null=True)
    