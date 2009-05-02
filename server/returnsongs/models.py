from django.db import models

# Create your models here.

class SongTag(models.Model):
    name = models.CharField()
    path = models.FilePathField()
    slope = models.FloatField()
    max_list = models.ForeignKey(TagsMaxList)
    min_list = models.ForeignKey(TagsMinList)    
    
class TagsMaxList(models.Model):
    max_list = models.FloatField()
    
class TagsMinList(models.Model):
    min_list = models.FloatField()

