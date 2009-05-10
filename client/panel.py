import wx
import Tkinter, tkSnack
import process
import search


class TunePanel(wx.StaticBoxSizer) :
  def __init__ (self,Frame,Panel):
    self.ASH_Frame = Frame
    wx.StaticBoxSizer.__init__(self,wx.StaticBox(Panel, -1, label='Tune'), wx.VERTICAL)
    self.Time = wx.StaticText(Panel, label="Time : 0 Sec")
    self.Title = wx.StaticText(Panel, size=(250,20), label="untitled.wav", style=wx.ALIGN_CENTER)
    Img = wx.Image('icons/wave.png',wx.BITMAP_TYPE_PNG)
    self.Waveform = wx.StaticBitmap(Panel, -1, Img.ConvertToBitmap())
    self.Add(self.Time, 0, wx.ALL, border=5)
    self.Add(self.Waveform, 0, wx.ALL, border=5)
    self.Add(self.Title, 0, wx.BOTTOM, border=5)
    self.TuneName = None
    self.TkRoot = Tkinter.Tk()
    tkSnack.initializeSnack(self.TkRoot)
    self.SnackSound = tkSnack.Sound()


class SongPanel(wx.StaticBoxSizer):
  def __init__ (self,Frame,Panel):
    self.ASH_Frame = Frame
    wx.StaticBoxSizer.__init__(self, wx.StaticBox(Panel, -1, label='Song List'), wx.VERTICAL)
    self.SongList = wx.ListBox(Panel, id=1, size=(260,470), choices=["No Songs Selected"])
    self.Add(self.SongList, 0, wx.ALL, border=10)
    self.Songs = None
    self.SongList.Bind (wx.EVT_LISTBOX_DCLICK, self.PlaySong)
#    wx.EVT_COMMAND_LISTBOX_DCLICKED(1, self.PlaySong)
  
  def PlaySong(self, event):
    if self.Songs != None:
      Player = self.ASH_Frame.Tools.Player
      if Player != None:
        Player.Stop()
        Player = None
      
      SongIndex = self.SongList.GetSelections()[0]
      SongName = self.Songs.keys()[SongIndex]
      SongPath = self.Songs[SongName]
      ServerUrl = self.ASH_Frame.Search.LastSearchServer + "songs/"
      RequestUrl = ServerUrl+SongPath
      SongFile = open("saves/.temp.wav", "wb")
      
      import urllib
      Song = urllib.urlopen(ServerUrl+SongPath)
      SongFile.writelines(Song.read())
      SongFile.close()
      
      Player = wx.Sound("saves/.temp.wav")
      Player.Play()
      print "Playing Song : ", RequestUrl


class SearchPanel(wx.StaticBoxSizer):
  def __init__ (self,Frame,Panel):
    wx.StaticBoxSizer.__init__(self, wx.StaticBox(Panel, -1, label='Search Server'))
    self.ASH_Frame = Frame
    self.LastSearchServer = None
    List = self.GetList().keys()
    self.ServerList = wx.ComboBox(Panel, value=List[0], size=(150,10), choices=List, style=wx.CB_DROPDOWN)
    self.Search = wx.Button(Panel, label="Search", style=wx.BU_EXACTFIT)
    self.Search.Bind(wx.EVT_BUTTON, self.OnSearch)
    self.Add(self.ServerList, 0, wx.EXPAND|wx.ALL, border=5)
    self.Add(self.Search, 0, wx.EXPAND|wx.ALL, border=5)

  def GetList (self):
    import pickle
    FH = open(".log.ash","r")
    List = pickle.load(FH)
    FH.close()
    return List

  def OnSearch(self, event):
    ServerName =  self.ServerList.GetValue()
    ServerUrl = self.GetList()[ServerName]
    if self.ASH_Frame.Tune.TuneName == None:
      Dialog = wx.MessageDialog(None, 'No tune found', 'Tune Empty', wx.OK | wx.ICON_EXCLAMATION)
      Dialog.ShowModal()
      return
    #self.SnackSound.configure(channels=1, frequency=22050, fileformat='WAV', encoding='Lin8')
    T = process.Tag(self.ASH_Frame.Tune.SnackSound)
    T.calculate_slope()
    T.calculate_max_min()
    Songs = search.GetSongs(T,ServerUrl)
    if Songs == -1:
      DisplayError("Cannot connect to server - \n"+ServerUrl)
      del(T)
      return
    if len(Songs) != 0:
      self.ASH_Frame.Song.SongList.Set(Songs.keys())
      self.ASH_Frame.Song.Songs = Songs
    self.LastSearchServer = ServerUrl
    del(T)

  def DisplayError(ErrorMessage):
    Dialog = wx.MessageDialog(None, ErrorMessage, 'Error!', wx.OK | wx.ICON_ERROR)
    Dialog.ShowModal()
