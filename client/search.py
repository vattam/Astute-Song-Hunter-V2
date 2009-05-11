def GetSongs(T, ServerName):

  import urllib

  if ServerName[-1] != '/':
    ServerName += '/'

  ServerName += "ash/retrievesongs/"
  Post = urllib.urlencode({'Slope' : T.Slope, 'MaxVar' : T.Max_List, 'MinVar' : T.Min_List })

  try :
    Response = urllib.urlopen(ServerName,Post)
  except IOError:
    return -1

  Data = Response.read()
  f = open("some.html","w")
  f.writelines(Data)
  f.close()
  
  SongList = {}
  if Data:
      for S in Data[1:-1].split(")("):
          Song, Path = tuple(S.split(","))
          SongList[Song[2:-1]] = Path[3:-1]
  
  return SongList
