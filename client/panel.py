import wx
import Tkinter, tkSnack


class TunePanel(wx.BoxSizer) :
  def __init__ (self,Frame,Panel):
    wx.BoxSizer.__init__(self,wx.VERTICAL)
    self.Timer = wx.StaticText(Panel, label="Time : 15 Sec")
    self.Title = wx.StaticText(Panel, label="untitled.wav", style=wx.ALIGN_LEFT)
    Img = wx.Image('icons/wave.png',wx.BITMAP_TYPE_PNG)
    self.Waveform = wx.StaticBitmap(Panel, -1, Img.ConvertToBitmap())
    self.Add(self.Timer,0,wx.EXPAND)
    self.Add(self.Waveform,0,wx.EXPAND)
    self.Add(self.Title,0,wx.EXPAND)

    SearchBox = wx.StaticBoxSizer(wx.StaticBox(Panel, -1, size=(-1,70), label='Search Server'))
    self.ServerList = wx.ComboBox(Panel, value="localhost",size=(100,10), choices=["localhost"], style=wx.CB_READONLY|wx.CB_DROPDOWN)
    self.Search = wx.Button(Panel, label="Search", style=wx.BU_EXACTFIT)
    SearchBox.Add(self.ServerList, 0, wx.EXPAND|wx.ALL, border=5)
    SearchBox.Add(self.Search, 0, wx.EXPAND|wx.ALL, border=5)
    self.Add(SearchBox, 0, wx.TOP, border=10)

    self.TuneName = None
    Root = Tkinter.Tk()
    tkSnack.initializeSnack(Root)
    self.SnackSound = tkSnack.Sound()


class SongPanel (wx.BoxSizer):
  def __init__ (self,Frame,Panel):
    wx.BoxSizer.__init__(self,wx.VERTICAL)
    self.Title = wx.StaticText(Panel, style=wx.ALIGN_CENTRE, label="Song List")
    self.SongList = wx.ListBox(Panel, size=(-1,100), choices=["No Songs Selected"])
    self.Add(self.Title, proportion=0, flag=wx.EXPAND)
    self.Add(self.SongList, proportion=1, flag=wx.EXPAND)
