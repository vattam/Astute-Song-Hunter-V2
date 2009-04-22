import wx
import files

class MainMenu(wx.MenuBar) :

  def __init__(self,Frame):
    wx.MenuBar.__init__(self)
    self.ASH_Frame = Frame

    (ID_NEW, ID_LOAD, ID_SAVE, ID_SAVE_AS, ID_QUIT) = (101, 102, 103, 104, 105)
    (ID_ABOUT) = (201)

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

    Helpmenu = wx.Menu()
    Helpmenu.Append(ID_ABOUT, "&About\tCtrl+H", " Information about the software")
    Frame.Bind(wx.EVT_MENU, self.OnAbout, id=ID_ABOUT)
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

