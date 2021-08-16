
# Create your models here.
from django.db import models
 
# Create your models here.
 
 
class News(models.Model):
    name = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)
    composition = models.CharField(max_length=255)

class Empsearch(models.Model):
    empname = models.CharField(max_length=255)
    empquality = models.CharField(max_length=255)
    empcomposition = models.CharField(max_length=255)    
    
    def __str__(self):
        return self.title
