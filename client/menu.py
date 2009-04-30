import wx
import files

class MainMenu(wx.MenuBar) :

  def __init__(self,Frame):
    wx.MenuBar.__init__(self)
    self.ASH_Frame = Frame

    (ID_NEW, ID_LOAD, ID_SAVE, ID_SAVE_AS, ID_QUIT) = (101, 102, 103, 104, 105)
    (ID_ADD) = (201)
    (ID_ABOUT,ID_DOC) = (301, 302)

    Filemenu = wx.Menu()
    Filemenu.Append(ID_NEW, "&New\tCtrl+N"," Create new a file")
    Filemenu.Append(ID_LOAD, "&Load\tCtrl+L"," Open a file to edit")
    Filemenu.Append(ID_SAVE, "&Save\tCtrl+S"," Save file")
    Filemenu.Append(ID_SAVE_AS, "Save &As\tCtrl+A"," Save file as")
    Filemenu.Append(ID_QUIT,"&Exit\tCtrl+E"," Terminate the program")
#    Filemenu.AppendSeparator()
    Frame.Bind(wx.EVT_MENU, self.OnNew, id=ID_NEW)
    Frame.Bind(wx.EVT_MENU, self.OnOpen, id=ID_LOAD)
    Frame.Bind(wx.EVT_MENU, self.OnExit, id=ID_QUIT)
    Frame.Bind(wx.EVT_MENU, self.OnSave, id=ID_SAVE)
    Frame.Bind(wx.EVT_MENU, self.OnSaveAs, id=ID_SAVE_AS)
    self.Append(Filemenu,"&File")

    Settingsmenu = wx.Menu()
    Settingsmenu.Append(ID_ADD, "&Add Server\tCtrl+A", " Add a media server to search")
    Frame.Bind(wx.EVT_MENU, self.OnAdd, id=ID_ADD)
    self.Append(Settingsmenu,"&Settings")


    Helpmenu = wx.Menu()
    Helpmenu.Append(ID_ABOUT, "&About\tCtrl+H", " Information about the software")
    Helpmenu.Append(ID_DOC, "&Documentation\tCtrl+D", " A view of Documentation")
    Frame.Bind(wx.EVT_MENU, self.OnAbout, id=ID_ABOUT)
    Frame.Bind(wx.EVT_MENU, self.OnDoc, id=ID_DOC)
    self.Append(Helpmenu,"&Help")


  def OnAbout(self,event):
    Description = """Astute Song Hunter is a tune based search engine that allows the user to search a song in a media database using the hummed tune. This software is completely built using python programming laguage."""
    Licence = """This is a free and open source software; you can redistribute it and/or modify it 
under the terms of the GNU General Public License as published by the Free Software Foundation; 
either version 2 of the License, or (at your option) any later version."""
    Help = wx.AboutDialogInfo()
    Help.SetIcon(wx.Icon('icons/ash.jpeg', wx.BITMAP_TYPE_JPEG))
    Help.SetName('Astute Song Hunter')
    Help.SetVersion('1.0')
    Help.SetDescription(Description)
    Help.SetWebSite('http://code.google.com/p/astute-song-hunter/')
    Help.SetLicence(Licence)
    Help.AddDeveloper("Madhusudan C. S\nPuneeth Bhat\nSantosh G. Vattam")
    wx.AboutBox(Help)

  def OnNew(self,event):
    self.ASH_Frame = None
    self.ASH_Frame.Tune.TuneFile = None


  def OnExit(self,event):
    ExitModal = wx.MessageDialog(self," Are you sure to exit?","Quit Dialog", wx.YES_NO)
    Response = ExitModal.ShowModal()
    if Response == wx.ID_YES:
      self.EditorFrame.Close(True)


  def OnOpen(self,event):
    files.OpenFile(self.ASH_Frame)


  def OnSave(self,event):
    files.SaveFile(self.ASH_Frame)


  def OnSaveAs(self,event):
    files.SaveFileAs(self.ASH_Frame)


  def OnAdd(self,event):
    AddServer = wx.Dialog(self.ASH_Frame, title="Add Server", size=(256,256))
    panel = wx.Panel(AddServer,-1)
    vbox = wx.BoxSizer(wx.VERTICAL)
    wx.StaticBox(panel,-1, 'Select Server',(5,5), (240,180))
    wx.StaticText(panel,-1, 'Enter the Server URL',(60,75),style=wx.ALIGN_CENTER)
    wx.StaticText(panel,-1, 'Name:',(50,110))
    wx.StaticText(panel,-1, 'URL:',(55,150))
    wx.TextCtrl(panel,-1, '',(95,105), name='Name')
    wx.TextCtrl(panel,-1, '',(95,145), name='URL')
    
    def closeServer(event):
      AddServer.Close()
    hbox = wx.BoxSizer(wx.HORIZONTAL)
    okButton = wx.Button(AddServer, -1, 'Select', size=(70, 30))
    closeButton = wx.Button(AddServer, -1, 'Close', size=(70, 30))
    closeButton.Bind(wx.EVT_BUTTON, closeServer)
    okButton.SetDefault()
    hbox.Add(okButton, 1, wx.LEFT)
    hbox.Add(closeButton, 1, wx.LEFT, 5)
    
    vbox.Add(panel)
    vbox.Add(hbox, 1, wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, 10)
    AddServer.SetSizer(vbox)
    AddServer.ShowModal()

  
#    """Under Construction"""
    
  def OnDoc(self,event):
    """Under Construction"""

