import wx
#import files

class MainMenu(wx.MenuBar) :

  def __init__(self,Frame):
    wx.MenuBar.__init__(self)
    self.dirname = ''
    self.EditorFrame = Frame

    (ID_NEW, ID_OPEN, ID_SAVE, ID_SAVE_AS, ID_PRINT, ID_QUIT) = (101, 102, 103, 104, 105, 106)
    (ID_UNDO, ID_REDO, ID_CUT, ID_COPY, ID_PASTE, ID_SELECT_ALL) = (201, 202, 203, 204, 205, 206)
    (ID_CHANGE, ID_ADD) = (401, 402)
    (ID_ABOUT) = (501)

    Filemenu = wx.Menu()
    Filemenu.Append(ID_NEW, "&New\tCtrl+N"," Create new a file")
    Filemenu.Append(ID_OPEN, "&Load\tCtrl+L"," Open a file to edit")
    Filemenu.Append(ID_SAVE, "&Save\tCtrl+S"," Save file")
    Filemenu.Append(ID_SAVE_AS, "Save &As\tCtrl+A"," Save file as")
    Filemenu.Append(ID_QUIT,"&Exit\tCtrl+E"," Terminate the program")
    Filemenu.AppendSeparator()
    Frame.Bind(wx.EVT_MENU, self.OnNew, id=ID_NEW)
    Frame.Bind(wx.EVT_MENU, self.OnOpen, id=ID_OPEN)
    Frame.Bind(wx.EVT_MENU, self.OnExit, id=ID_QUIT)
    Frame.Bind(wx.EVT_MENU, self.OnSave, id=ID_SAVE)
    Frame.Bind(wx.EVT_MENU, self.OnSave, id=ID_SAVE_AS)
    self.Append(Filemenu,"&File")

    Editmenu = wx.Menu()
    Editmenu.Append(ID_CUT, "&Cut\tCtrl+X"," Cut the slected part")
    Editmenu.Append(ID_COPY, "C&opy\tCtrl+C"," Copy the selected part")
    Editmenu.Append(ID_PASTE,"&Paste\tCtrl+V"," Paste the select")
    Editmenu.AppendSeparator()
    Editmenu.Append(ID_SELECT_ALL, "Select &All\tCtrl+A"," Select entire file")
#    Frame.Bind(wx.EVT_MENU, self.OnCut, id=ID_CUT)
#    Frame.Bind(wx.EVT_MENU, self.OnCopy, id=ID_COPY)
#    Frame.Bind(wx.EVT_MENU, self.OnPaste, id=ID_PASTE)
#    Frame.Bind(wx.EVT_MENU, self.OnSelectAll, id=ID_SELECT_ALL)
    self.Append(Editmenu,"&Edit")

    Helpmenu = wx.Menu()
    Helpmenu.Append(ID_ABOUT, "&About\tCtrl+H", " Information about the software")
    Frame.Bind(wx.EVT_MENU, self.OnAbout, id=ID_ABOUT)
    self.Append(Helpmenu,"&Help")


  def OnAbout(self,event):
    AboutMe = wx.MessageDialog(self," A sample editor \nin wxPython","About Sample Editor", wx.OK)
    AboutMe.ShowModal()

  def OnNew(self,event):
    "Under Construction"

  def OnExit(self,event):
    ExitModal = wx.MessageDialog(self," Are you sure to exit?","Quit Dialog", wx.YES_NO)
    Response = ExitModal.ShowModal()
    if Response == wx.ID_YES:
      self.EditorFrame.Close(True)

  def OnOpen(self,event):
    "Under Construction"

  def OnSave(self,event):
    "Under Construction"

