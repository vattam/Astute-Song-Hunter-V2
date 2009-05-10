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
    Frame.Bind(wx.EVT_TOOL, self.OnSaveSong, id=ID_DOWNLOAD)
    self.Realize()
    self.Player = None


  def OnNew(self,event):
    files.OnNew(self.ASH_Frame)


  def OnOpen(self,event):
    files.OpenFile(self.ASH_Frame)


  def OnSave(self,event):
    files.SaveFile(self.ASH_Frame)


  def OnPlay(self,event):
    if self.ASH_Frame.Tune.TuneName != None:
      self.Player = wx.Sound(self.ASH_Frame.Tune.TuneName)
      self.Player.Play()


  def OnStop(self,event):
    if self.Player != None:
      self.Player.Stop()
      self.Player = None


  def OnRecord(self,event):
    import tune, Tkinter, tkSnack
    tune.recorder(self.ASH_Frame)
    self.ASH_Frame.Tune.TuneName = "saves/.temp.wav"
    self.ASH_Frame.Tune.TkRoot = Tkinter.Tk()
    tkSnack.initializeSnack(self.ASH_Frame.Tune.TkRoot)
    Time = "Time : " + str(self.ASH_Frame.Tune.SnackSound.length(unit="SECONDS")) + "Sec"
    self.ASH_Frame.Tune.Time.SetLabel(Time)
    self.ASH_Frame.Tune.DrawGraph()


  def OnSaveSong(self, event):
    S = self.ASH_Frame.Song.SongList.GetSelections()
    if self.ASH_Frame.Song.Songs == None or S == ():
      Dialog = wx.MessageDialog(None, "No Song Selected.", 'Error!', wx.OK | wx.ICON_ERROR)
      Dialog.ShowModal()
    else:
      files.SaveSong(self.ASH_Frame)
