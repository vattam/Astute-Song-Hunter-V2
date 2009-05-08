from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

from server.returnsongs.models import SongTag, TagsMinList, TagsMaxList
from server.returnsongs.all import main
from server.returnsongs.search import SearchTune

# Create your views here.
def bulk_add_tags(request):
    return render_to_response('returnsongs/bulk-add.html')

def tags_added(request):
    tag_dir = request.POST['tagdir']
    
    if tag_dir[-1] != '/':
        tag_dir = tag_dir + '/'
    
    tag_data = main(tag_dir)
    
    for tag in tag_data:
        tag_db = SongTag(name=tag['Name'], path=tag['Path'], slope=tag['Slope'])
        tag_db.save()
        
        for max_value in tag['MaxList']:
            tag_db.tagsmaxlist_set.create(max_value=max_value)
        
        for min_list in tag['MinList']:
            tag_db.tagsminlist_set.create(min_value=min_value)

    return HttpResponse(len(tag_data))

def retrievesongs(request):
    hum_slope = request.POST['Slope']
    hum_maxvar = request.POST['MaxVar']
    hum_minvar = request.POST['MinVar']
    
    stune = SongTune(hum_slope, hum_maxvar, hum_minvar)
    
    selected_songs = []
    
    stags = SongTag.objects.all()
    for stag in stags:
        if stune.SearchByRegression(stag.Slope) and stune.FindMaxMin(
          stune.getTagsMaxList(), stune.getTagsMinList()):
            selected_songs.append((stag.name, stag.path))

    
    return HttpResponse(selected_songs)
