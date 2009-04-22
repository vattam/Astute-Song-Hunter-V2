import os
import wx

DirName = "."
FileName = "untitled"
Filters = ["*.wav"]


def Open(Frame):
  global FileName, DirName
  F = DirName+"/"+FileName
  Frame.Tune.TuneName = F
  Frame.Tune.SnackSound.read(F)
  Frame.Tune.Title.SetLabel(F)


def OpenFile(Frame):
  global FileName, DirName, Filters
  OpenDialog = wx.FileDialog(Frame,"Open a tune", DirName, '', "*.wav", wx.OPEN)
  if OpenDialog.ShowModal() == wx.ID_OK:
    DirName = OpenDialog.GetDirectory()
    FileName = OpenDialog.GetFilename()
    Open(Frame)
  OpenDialog.Destroy()


def SaveFile(Frame):
  global FileName, DirName
  if FileName != "untitled":
    Save(Frame)
  else :
    SaveDialog = wx.FileDialog(Frame, "Save the file", DirName, FileName, "*.wav", wx.SAVE | wx.OVERWRITE_PROMPT)
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
  if FileName.endswith(".wav"):
    F = DirName+"/"+FileName
  else:
    F = DirName+"/"+FileName+".wav"
  Frame.Tune.SnackSound.write(F,fileformat="wav")
  Frame.Tune.Title.SetLabel(F)
