from django.db import models

# Create your models here.

class Blog(models.Model):
  owner = models.CharField(max_length=255)
  title = models.CharField(max_length=255)
  description = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)