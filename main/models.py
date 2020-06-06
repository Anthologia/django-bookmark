from django.db import models

# Create your models here.

class Bookmark(models.Model):
    site_name = models.CharField(max_length=50)
    site_url = models.CharField(max_length=1000)