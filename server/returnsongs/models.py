from django.db import models

# Create your models here.  
class SongTag(models.Model):
    name = models.CharField(max_length=128)
    path = models.FilePathField(max_length=1024)
    slope = models.FloatField()
    
    def getTagsMaxList(self):
        tmaxlist = self.tagsmaxlist_set.all()
        
        max_vals = []
        for tmax in tmaxlist:
            max_vals.append(tmax.max_value)
        
        return max_vals
    
    def getTagsMinList(self):
        tminlist = self.tagsminlist_set.all()
        
        min_vals = []
        for tmin in tminlist:
            min_vals.append(tmin.min_value)
        
        return min_vals        
    

class TagsMaxList(models.Model):
    song = models.ForeignKey(SongTag)
    max_value = models.FloatField()

    
class TagsMinList(models.Model):
    song = models.ForeignKey(SongTag)
    min_value = models.FloatField()

