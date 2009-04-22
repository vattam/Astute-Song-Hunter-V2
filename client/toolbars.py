import wx
import files

class Toolbar(wx.ToolBar):
  def __init__(self,Frame,Panel):
    self.ASH_Frame = Frame
    wx.ToolBar.__init__(self,Panel, id=-1, style = wx.TB_HORIZONTAL | wx.TB_TEXT)
    (ID_NEW,ID_OPEN,ID_SAVE) = (1,2,3)
    self.AddLabelTool(ID_NEW,'New', wx.Bitmap('icons/new.png'))
    self.AddLabelTool(ID_OPEN, 'Open', wx.Bitmap('icons/open.png'))
    self.AddLabelTool(ID_SAVE, 'Save', wx.Bitmap('icons/save.png'))
    self.AddSeparator()
    Frame.Bind(wx.EVT_TOOL, self.OnNew, id=ID_NEW)
    Frame.Bind(wx.EVT_TOOL,self.OnOpen, id=ID_OPEN)
    Frame.Bind(wx.EVT_TOOL,self.OnSave, id=ID_SAVE)
    self.Realize()


  def OnNew(self,event):
    self.ASH_Frame.Tune.TuneName = None


  def OnOpen(self,event):
    files.OpenFile(self.ASH_Frame)


  def OnSave(self,event):
    files.SaveFile(self.ASH_Frame)

