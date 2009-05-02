from django.db import models

# Create your models here.  
class TagsMaxList(models.Model):
    max_list = models.FloatField()
    
class TagsMinList(models.Model):
    min_list = models.FloatField()

class SongTag(models.Model):
    name = models.CharField(max_length=128)
    path = models.FilePathField(max_length=1024)
    slope = models.FloatField()
    max_list = models.ForeignKey(TagsMaxList)
    min_list = models.ForeignKey(TagsMinList)    

