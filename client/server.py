import wx
import pickle


class AddDialog (wx.Dialog):

  def __init__ (self, Frame):
      wx.Dialog.__init__(self, Frame, title="Add Server Address", size=(256,256))
      self.ASH_Frame = Frame
      NewPanel = wx.Panel(self, -1)
      VBox = wx.BoxSizer(wx.VERTICAL)
      wx.StaticBox(NewPanel, -1, 'Insert Server',(5,5), (240,180))
      wx.StaticText(NewPanel, -1, 'Enter the Server URL',(60,40),style=wx.ALIGN_CENTER)
      wx.StaticText(NewPanel, -1, 'Name:',(30,100))
      wx.StaticText(NewPanel, -1, 'URL:',(35,150))
      self.ServerName = wx.TextCtrl(NewPanel, -1, '', (85,95), size=(150,30))
      self.Url = wx.TextCtrl(NewPanel, -1, '', (85,145), size=(150,30))
      HBox = wx.BoxSizer(wx.HORIZONTAL)
      OkButton = wx.Button(self, -1, 'Ok')
      OkButton.Bind(wx.EVT_BUTTON, self.AddServer)
      CloseButton = wx.Button(self, -1, 'Cancel')
      CloseButton.Bind(wx.EVT_BUTTON, self.CloseServer)
      CloseButton.SetDefault()
      HBox.Add(OkButton, 1, wx.LEFT)
      HBox.Add(CloseButton, 1, wx.LEFT, 5)
      VBox.Add(NewPanel)
      VBox.Add(HBox, 1, wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, 10)
      self.SetSizer(VBox)

  def Display(self):
    self.ShowModal()

  def CloseServer(self, event):
    self.Close()

  def AddServer(self, event):
    Name = self.ServerName.GetValue()
    Url = self.Url.GetValue()
    if Name == "" or Url == "":
      self.DisplayError('Some fields missing!')
      return
    FH = open(".log.ash","r")
    ServerList = pickle.load(FH)
    FH.close()
    if Name in ServerList.keys():
      self.DisplayError('Duplicate server Names')
      return
    ServerList[Name] = Url
    FH = open(".log.ash","w")
    pickle.dump(ServerList, FH)
    FH.close()
#    self.ASH_Frame.Tune.ServerList.SetValue(Name)
    self.Close()

  def DisplayError(self, ErrorMessage):
    Dialog = wx.MessageDialog(None, ErrorMessage, 'Error!', wx.OK | wx.ICON_ERROR)
    Dialog.ShowModal()


class RemoveDialog (wx.Dialog):

  def __init__ (self, Frame):
      wx.Dialog.__init__(self, Frame, title="Remove Server Address", size=(256,180))
      self.ASH_Frame = Frame
      NewPanel = wx.Panel(self, -1)
      VBox = wx.BoxSizer(wx.VERTICAL)
      wx.StaticBox(NewPanel, -1, 'Remove Server',(5,5), (240,120))
      wx.StaticText(NewPanel, -1, 'Select the server to remove',(30,40),style=wx.ALIGN_CENTER)
      List = self.GetList()
      self.ServerList = wx.ComboBox(NewPanel, value="localhost", pos=(50,65), size=(150,30), choices=List, style=wx.CB_DROPDOWN)
      HBox = wx.BoxSizer(wx.HORIZONTAL)
      OkButton = wx.Button(self, -1, 'Remove')
      OkButton.Bind(wx.EVT_BUTTON, self.RemoveServer)
      CloseButton = wx.Button(self, -1, 'Cancel')
      CloseButton.Bind(wx.EVT_BUTTON, self.CloseServer)
      CloseButton.SetDefault()
      HBox.Add(OkButton, 1, wx.LEFT)
      HBox.Add(CloseButton, 1, wx.LEFT, 5)
      VBox.Add(NewPanel)
      VBox.Add(HBox, 1, wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, 10)
      self.SetSizer(VBox)

  def GetList (self):
    import pickle
    FH = open(".log.ash","r")
    List = pickle.load(FH)
    FH.close()
    return List.keys()

  def Display(self):
    self.ShowModal()

  def CloseServer(self, event):
    self.Close()

  def RemoveServer(self, event):
    Name = self.ServerList.GetValue()
    FH = open(".log.ash","r")
    ServerList = pickle.load(FH)
    FH.close()
    ServerList.pop(Name)
    FH = open(".log.ash","w")
    pickle.dump(ServerList, FH)
    FH.close()
    self.Close()

  def DisplayError(self, ErrorMessage):
    Dialog = wx.MessageDialog(None, ErrorMessage, 'Error!', wx.OK | wx.ICON_ERROR)
    Dialog.ShowModal()
