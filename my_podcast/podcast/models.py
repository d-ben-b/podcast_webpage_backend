from django.db import models

# Create your models here.
class Podcast(models.Model):
  title = models.CharField(max_length=100)
  about = models.CharField(max_length=1000)
  version = models.IntegerField(null=True)
  record_time = models.DateTimeField(auto_now_add=True, null=True)
  
