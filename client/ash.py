import wx
from menu import MainMenu
from toolbars import Toolbar
from panel import TunePanel
from panel import SongPanel
from panel import SearchPanel
from splash import SplashScreen


class MainFrame(wx.Frame):
  def __init__(self):
    wx.Frame.__init__(self,None, size=(600,600), title="Astute Song Hunter", style=wx.DEFAULT_FRAME_STYLE & ~(wx.MAXIMIZE_BOX|wx.RESIZE_BORDER))
    self.Menubar = MainMenu(self)
    self.SetMenuBar(self.Menubar)
    self.MainPanel = wx.Panel(self)
    self.Tools = Toolbar(self,self.MainPanel)
    self.Tune = TunePanel(self,self.MainPanel)
    self.Song = SongPanel(self,self.MainPanel)
    self.Search = SearchPanel(self, self.MainPanel)
    self.SetToolBar(self.Tools)
    VBox = wx.BoxSizer(wx.VERTICAL)
    VBox.Add(self.Tune, proportion=0, flag=wx.BOTTOM|wx.LEFT, border=10)
    VBox.Add(self.Search, proportion=0, flag=wx.LEFT|wx.TOP, border=20)
    HBox = wx.BoxSizer()
    HBox.Add(VBox, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
    HBox.Add(self.Song, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
    self.MainPanel.SetSizer(HBox)
    self.Centre()
#    self.Maximize(True)
    self.Show(True)


ASH = wx.App()
ASH_Frame = MainFrame()
#Splash = SplashScreen(ASH_Frame)
ASH.MainLoop()

