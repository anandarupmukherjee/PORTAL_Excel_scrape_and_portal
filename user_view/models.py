
# Create your models here.
from django.db import models
 
# Create your models here.
 

class Profile(models.Model):
   name = models.CharField(max_length = 50)
   picture = models.FileField(upload_to = 'original')
   class Meta:
      db_table = "profile"


 
class News(models.Model):
    name = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)
    composition = models.CharField(max_length=255)
    process1a = models.CharField(max_length=255)
    process1b = models.CharField(max_length=255)
    process1c = models.CharField(max_length=255)
    process2a = models.CharField(max_length=255)
    process2b = models.CharField(max_length=255)
    process2c = models.CharField(max_length=255)
    process3a = models.CharField(max_length=255)
    process3b = models.CharField(max_length=255)
    process3c = models.CharField(max_length=255)
    proc_info1 = models.CharField(max_length=255)
    proc_info2 = models.CharField(max_length=255)

class Empsearch(models.Model):
    empname = models.CharField(max_length=255)
    empquality = models.CharField(max_length=255)
    empcomposition = models.CharField(max_length=255)    
    
    def __str__(self):
        return self.title
