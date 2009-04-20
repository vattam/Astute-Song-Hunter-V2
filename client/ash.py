import wx
from menu import MainMenu
from toolbars import Toolbar
from panel import TunePanel
from panel import SongPanel


class MainFrame(wx.Frame):
  def __init__(self):
    wx.Frame.__init__(self,None,title="Astute Song Hunter",style=wx.DEFAULT_FRAME_STYLE)
    self.Menubar = MainMenu(self)
    self.SetMenuBar(self.Menubar)
    BackPanel = wx.Panel(self)
    self.Tools = Toolbar(self,BackPanel)
    self.Tune = TunePanel(self,BackPanel)
    self.Song = SongPanel(self,BackPanel)
    self.SetToolBar(self.Tools)
    VBox = wx.BoxSizer()
    VBox.Add(self.Tune,1,wx.EXPAND)
    VBox.Add(self.Song,1,wx.EXPAND|wx.ALIGN_CENTER_VERTICAL)
    BackPanel.SetSizer(VBox)
    self.Centre()
#    self.Maximize(True)
    self.Show(True)


ASH = wx.App()
ASH_Frame = MainFrame()
ASH.MainLoop()
