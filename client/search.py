def GetSongs(T, ServerName):

  import urllib

  if ServerName[-1] != '/':
    ServerName += '/'

  ServerName += "ash/retrievesongs/"
  Post = urllib.urlencode({'Slope' : T.Slope, 'MaxList' : T.Max_List, 'MinList' : T.Min_List })

  try :
    Response = urllib.urlopen(ServerName,Post)
  except IOError:
    return -1

  Data = Response.read()
  return {"Song_1.mp3":1, "Song_2.mp3":2, "Song_3.mp3":3, "Song_4.mp3":4, "Song_5.mp3":4}
