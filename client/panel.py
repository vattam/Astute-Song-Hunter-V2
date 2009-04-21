import wx

class TunePanel(wx.BoxSizer) :
  def __init__ (self,Frame,Panel):
    wx.BoxSizer.__init__(self,wx.VERTICAL)
    self.Timer = wx.StaticText(Panel, label="Time : 15 Sec")
    Img = wx.Image('icons/wave.png',wx.BITMAP_TYPE_PNG)
    self.Waveform = wx.StaticBitmap(Panel, -1, Img.ConvertToBitmap())
    Player = wx.BoxSizer()
    self.Play = wx.Button(Panel, label="Play", style=wx.BU_EXACTFIT)
    self.Record = wx.Button(Panel, label="Record", style=wx.BU_EXACTFIT)
    self.Stop = wx.Button(Panel, label="Stop", style=wx.BU_EXACTFIT)
    Player.Add(self.Play, 0, wx.EXPAND)
    Player.Add(self.Stop, 0, wx.EXPAND)
    Player.Add(self.Record, 0, wx.EXPAND)
    self.Add(self.Timer,0,wx.EXPAND)
    self.Add(self.Waveform,0,wx.EXPAND)
    self.Add(Player,0,wx.EXPAND)


class SongPanel (wx.BoxSizer):
  def __init__ (self,Frame,Panel):
    wx.BoxSizer.__init__(self,wx.VERTICAL)
    self.Title = wx.StaticText(Panel, style=wx.ALIGN_CENTRE, label="Song List")
    self.SongList = wx.ListBox(Panel, size=(-1,100), choices=["No Songs Selected"])
    Player = wx.BoxSizer()
    self.Play = wx.Button(Panel, label="Play", style=wx.BU_EXACTFIT)
    self.Download = wx.Button(Panel, label="Save", style=wx.BU_EXACTFIT)
    self.Stop = wx.Button(Panel, label="Stop", style=wx.BU_EXACTFIT)
    Player.Add(self.Play, 0, wx.EXPAND)
    Player.Add(self.Stop, 0, wx.EXPAND)
    Player.Add(self.Download, 0, wx.EXPAND)
    self.Add(self.Title, proportion=0, flag=wx.EXPAND)
    self.Add(self.SongList, proportion=1, flag=wx.EXPAND)
    self.Add(Player, proportion=0, flag=wx.EXPAND)
