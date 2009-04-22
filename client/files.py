import os
import wx

DirName = "."
FileName = "untitled"
Filters = ["*.wav"]


def Open(Frame):
  global FileName, DirName
  Frame.Tune.TuneName = DirName+"/"+FileName

def OpenFile(Frame):
  global FileName, DirName, Filters
  OpenDialog = wx.FileDialog(Frame,"Open a tune", DirName, '', "*.*", wx.OPEN)
  if OpenDialog.ShowModal() == wx.ID_OK:
    DirName = OpenDialog.GetDirectory()
    FileName = OpenDialog.GetFilename()
    Open(Frame)
  OpenDialog.Destroy()


def SaveFile(Frame):
  global FileName, DirName
  if FileName != "":
    Save(Frame)
  else :
    SaveDialog = wx.FileDialog(Frame, "Save the file", DirName, FileName, "*.*", wx.SAVE | wx.OVERWRITE_PROMPT)
    if SaveDialog.ShowModal() == wx.ID_OK:
      DirName = SaveDialog.GetDirectory()
      FileName = SaveDialog.GetFilename()
      Save(Frame)
    SaveDialog.Destroy()


def SaveFileAs(Frame):
  global FileName, DirName
  SaveDialog = wx.FileDialog(Frame, "Save the file", DirName, FileName, "*.*", wx.SAVE | wx.OVERWRITE_PROMPT)
  if SaveDialog.ShowModal() == wx.ID_OK:
    DirName = SaveDialog.GetDirectory()
    FileName = SaveDialog.GetFilename()
    Save(Frame)
  SaveDialog.Destroy()


def Save(Frame):
  global FileName, DirName
  FH = file(DirName+"/"+FileName,"w")
  pickle.dump(Frame.TextEdit.Text.KanadaLines,FH)
  pickle.dump(Frame.TextEdit.Text.EnglishLines,FH)
  FH.close()


def ChangeLanguage(Frame,Language):
  Frame.TextEdit.Text.readUnicode(Language)
  Frame.TextEdit.Text.convertAll()
  Frame.TextEdit.ViewBox.SetValue(Frame.TextEdit.Text.ConvertedText)
