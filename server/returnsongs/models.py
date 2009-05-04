from django.db import models

# Create your models here.  
class SongTag(models.Model):
    name = models.CharField(max_length=128)
    path = models.FilePathField(max_length=1024)
    slope = models.FloatField()

class TagsMaxList(models.Model):
    song_id = models.ForeignKey(SongTag)
    max_value = models.FloatField()
    
class TagsMinList(models.Model):
    song_id = models.ForeignKey(SongTag)
    min_value = models.FloatField()

