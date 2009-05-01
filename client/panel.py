import wx
import Tkinter, tkSnack
import process
import search


class TunePanel(wx.BoxSizer) :
  def __init__ (self,Frame,Panel):
    self.ASH_Frame = Frame
    wx.BoxSizer.__init__(self,wx.VERTICAL)
    RecordBox = wx.StaticBoxSizer(wx.StaticBox(Panel, -1, label='Tune'), wx.VERTICAL)
    self.Time = wx.StaticText(Panel, label="Time : 15 Sec")
    self.Title = wx.StaticText(Panel, size=(250,20), label="untitled.wav", style=wx.ALIGN_CENTER)
    Img = wx.Image('icons/wave.png',wx.BITMAP_TYPE_PNG)
    self.Waveform = wx.StaticBitmap(Panel, -1, Img.ConvertToBitmap())
    RecordBox.Add(self.Time, 0, wx.ALL, border=5)
    RecordBox.Add(self.Waveform, 0, wx.ALL, border=5)
    RecordBox.Add(self.Title, 0, wx.BOTTOM, border=5)
    self.Add(RecordBox, 0, wx.TOP|wx.LEFT, border=10)

    SearchBox = wx.StaticBoxSizer(wx.StaticBox(Panel, -1, label='Search Server'))
    List = self.GetList().keys()
    self.ServerList = wx.ComboBox(Panel, value="localhost",size=(150,10), choices=List, style=wx.CB_DROPDOWN)
    self.Search = wx.Button(Panel, label="Search", style=wx.BU_EXACTFIT)
    self.Search.Bind(wx.EVT_BUTTON, self.OnSearch)
    SearchBox.Add(self.ServerList, 0, wx.EXPAND|wx.ALL, border=5)
    SearchBox.Add(self.Search, 0, wx.EXPAND|wx.ALL, border=5)
    self.Add(SearchBox, 0, wx.TOP|wx.LEFT, border=20)

    self.TuneName = None
    self.TkRoot = Tkinter.Tk()
    tkSnack.initializeSnack(self.TkRoot)
    self.SnackSound = tkSnack.Sound()

  def OnSearch(self, event):
    ServerName =  self.ServerList.GetValue()
    ServerUrl = self.GetList()[ServerName]
    if self.TuneName == None:
      Dialog = wx.MessageDialog(None, 'No tune found', 'Tune Empty', wx.OK | wx.ICON_EXCLAMATION)
      Dialog.ShowModal()
      return
    #self.SnackSound.configure(channels=1, frequency=22050, fileformat='WAV', encoding='Lin8')
    T = process.Tag(self.SnackSound)
    T.calculate_slope()
    T.calculate_max_min()
    Songs = search.GetSongs(T,ServerUrl)
    self.ASH_Frame.Song.SongList.Set(Songs)
    self.ASH_Frame.Song.Songs = Songs
    del(T)

  def GetList (self):
    import pickle
    FH = open(".log.ash","r")
    List = pickle.load(FH)
    FH.close()
    return List


class SongPanel(wx.StaticBoxSizer):
  def __init__ (self,Frame,Panel):
    wx.StaticBoxSizer.__init__(self, wx.StaticBox(Panel, -1, label='Song List'), wx.VERTICAL)
    self.SongList = wx.ListBox(Panel, size=(260,470), choices=["No Songs Selected"])
    self.Add(self.SongList, 0, wx.ALL, border=10)
    self.Songs = None
