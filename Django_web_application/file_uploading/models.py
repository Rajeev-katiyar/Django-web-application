

# Create your models here.
from django.db import models

class img_uploader(models.Model):
    imageFile = models.FileField(upload_to='uploader/')  # Use FileField for file uploads
