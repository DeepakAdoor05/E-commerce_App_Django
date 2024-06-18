from django.db import models

# Create your models here.

class Site_setting(models.Model):
    banner=models.ImageField(upload_to='media/site/')
    caption=models.TextField()