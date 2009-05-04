from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

from server.returnsongs.models import SongTag, TagsMinList, TagsMaxList
from server.returnsongs.all import main

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
    pass

## task to be done once a request is obtained

#1. say a client requests by posting a hums values in $POST (just say)

#2. create a new object ST = search.SongTune ($POST[Slope], $POST[MaxVar], $POST[MinVar])

#3. perform the query something like - 

    # List1 = select * from SongTag where ST.SearchByRegression(SongTag.Slope) is True;
    
    # List2 = select * from SongTag where ST.FindMaxMin (
    #           select * from TagsMaxList where SongId = SongTag.SongId, 
    #           select * from TagsMinList where SongId = SongTag.SongId
    #         ) is True;

#4. return Intersection of 2 lists

