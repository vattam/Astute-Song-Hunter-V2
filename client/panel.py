import wx
import Tkinter, tkSnack


class TunePanel(wx.BoxSizer) :
  def __init__ (self,Frame,Panel):
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
    self.ServerList = wx.ComboBox(Panel, value="localhost",size=(150,10), choices=["localhost"], style=wx.CB_READONLY|wx.CB_DROPDOWN)
    self.Search = wx.Button(Panel, label="Search", style=wx.BU_EXACTFIT)
    SearchBox.Add(self.ServerList, 0, wx.EXPAND|wx.ALL, border=5)
    SearchBox.Add(self.Search, 0, wx.EXPAND|wx.ALL, border=5)
    self.Add(SearchBox, 0, wx.TOP|wx.LEFT, border=20)

    self.TuneName = None
    self.TkRoot = Tkinter.Tk()
    tkSnack.initializeSnack(self.TkRoot)
    self.SnackSound = tkSnack.Sound()


class SongPanel(wx.StaticBoxSizer):
  def __init__ (self,Frame,Panel):
    wx.StaticBoxSizer.__init__(self, wx.StaticBox(Panel, -1, label='Song List'), wx.VERTICAL)
    self.SongList = wx.ListBox(Panel, size=(260,470), choices=["No Songs Selected"])
    self.Add(self.SongList, 0, wx.ALL, border=10)