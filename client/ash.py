import wx
from menu import MainMenu
from toolbars import Toolbar
from panel import TunePanel
from panel import SongPanel
from splash import SplashScreen


class MainFrame(wx.Frame):
  def __init__(self):
    wx.Frame.__init__(self,None, size=(600,600), title="Astute Song Hunter", style=wx.DEFAULT_FRAME_STYLE & ~(wx.MAXIMIZE_BOX|wx.RESIZE_BORDER))
    self.Menubar = MainMenu(self)
    self.SetMenuBar(self.Menubar)
    MainPanel = wx.Panel(self)
    self.Tools = Toolbar(self,MainPanel)
    self.Tune = TunePanel(self,MainPanel)
    self.Song = SongPanel(self,MainPanel)
    self.SetToolBar(self.Tools)
    VBox = wx.BoxSizer()
    VBox.Add(self.Tune, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
    VBox.Add(self.Song, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
    MainPanel.SetSizer(VBox)
    self.Centre()
#    self.Maximize(True)
    self.Show(True)


ASH = wx.App()
ASH_Frame = MainFrame()
#Splash = SplashScreen(ASH_Frame)
ASH.MainLoop()

