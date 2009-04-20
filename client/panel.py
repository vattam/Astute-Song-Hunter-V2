import wx

class TunePanel(wx.BoxSizer) :
  def __init__ (self,Frame,Panel):
    wx.BoxSizer.__init__(self)
    self.Waveform = wx.TextCtrl(Panel, size=(-1,100), style=wx.TE_MULTILINE | wx.HSCROLL | wx.TE_READONLY | wx.TE_MULTILINE)
    self.Add(self.Waveform,1,wx.EXPAND)


class SongPanel (wx.BoxSizer):
  def __init__ (self,Frame,Panel):
    wx.BoxSizer.__init__(self)
    self.SongList = wx.TextCtrl(Panel, size=(-1,100), style=wx.TE_MULTILINE | wx.HSCROLL | wx.TE_READONLY)
    self.Add(self.SongList,1,wx.EXPAND)
