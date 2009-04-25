import wx
import files

class Toolbar(wx.ToolBar):
  def __init__(self,Frame,Panel):
    self.ASH_Frame = Frame
    wx.ToolBar.__init__(self,Panel, id=-1, style = wx.TB_HORIZONTAL | wx.TB_TEXT)
    (ID_NEW,ID_OPEN,ID_SAVE,ID_PLAY,ID_STOP,ID_RECORD,ID_DOWNLOAD) = (1,2,3,4,5,6,7)
    self.AddLabelTool(ID_NEW,'New', wx.Bitmap('icons/new.png'))
    self.AddLabelTool(ID_OPEN, 'Open', wx.Bitmap('icons/open.png'))
    self.AddLabelTool(ID_SAVE, 'Save', wx.Bitmap('icons/save.png'))
    self.AddSeparator()
    self.AddLabelTool(ID_PLAY, 'Play', wx.Bitmap('icons/play.png'))
    self.AddLabelTool(ID_STOP, 'Stop', wx.Bitmap('icons/stop.png'))
    self.AddLabelTool(ID_RECORD, 'Record', wx.Bitmap('icons/record.png'))
    self.AddSeparator()
    self.AddLabelTool(ID_DOWNLOAD, 'Save Song', wx.Bitmap('icons/download.jpeg'))
    self.AddSeparator()    
    Frame.Bind(wx.EVT_TOOL, self.OnNew, id=ID_NEW)
    Frame.Bind(wx.EVT_TOOL, self.OnOpen, id=ID_OPEN)
    Frame.Bind(wx.EVT_TOOL, self.OnSave, id=ID_SAVE)
    Frame.Bind(wx.EVT_TOOL, self.OnPlay, id=ID_PLAY)
    Frame.Bind(wx.EVT_TOOL, self.OnStop, id=ID_STOP)
    Frame.Bind(wx.EVT_TOOL, self.OnRecord, id=ID_RECORD)
    self.Realize()
    self.Player = None


  def OnNew(self,event):
    self.ASH_Frame.Tune.TuneName = None


  def OnOpen(self,event):
    files.OpenFile(self.ASH_Frame)


  def OnSave(self,event):
    files.SaveFile(self.ASH_Frame)


  def OnPlay(self,event):
    S = self.ASH_Frame.Song.SongList.GetSelections()
    if self.ASH_Frame.Song.Songs == None or S == ():
      if self.ASH_Frame.Tune.TuneName != None:
        self.Player = wx.Sound(self.ASH_Frame.Tune.TuneName)
        self.Player.Play()
    else : 
      print self.ASH_Frame.Song.Songs[S]


  def OnStop(self,event):
    if self.Player != None:
      self.Player.Stop()
      self.Player = None


  def OnRecord(self,event):
    """Under construction"""
#    import tune
#    tune.recorder(self.ASH_Frame)
