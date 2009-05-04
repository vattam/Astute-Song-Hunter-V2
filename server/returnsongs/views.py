# Create your views here.

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
