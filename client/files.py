import os
import wx

DirName = "."
FileName = "untitled"
Filters = ["*.wav"]


def OnNew(Frame):
  DirName = "."
  FileName = "untitled"
  Frame.Tune.TuneName = None
  Frame.Song.Songs = None
  Frame.Song.SongList.Set(["No Songs Selected"])
  Frame.Tune.SnackSound.flush()
  Frame.Tune.Time.SetLabel("Time : 0 Sec")
  Frame.Tune.Title.SetLabel("untitled.wav")



def Open(Frame):
  global FileName, DirName
  F = DirName+"/"+FileName
  Frame.Tune.TuneName = F
  Frame.Tune.SnackSound.read(F)
  Frame.Tune.Title.SetLabel(F.split("/")[-1])
  Time = "Time : " + str(Frame.Tune.SnackSound.length(unit="SECONDS")) + "Sec"
  Frame.Tune.Time.SetLabel(Time)



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
  Frame.Tune.Title.SetLabel(F.split("/")[-1])


def SaveSong(Frame):
  global DirName
  SongIndex = Frame.Song.SongList.GetSelections()[0]
  FileName = Frame.Song.Songs.keys()[SongIndex]
  Format = FileName.split(".")[-1]
  Directory = DirName
  SaveDialog = wx.FileDialog(Frame, "Save the song file", DirName, FileName, "*.*", wx.SAVE | wx.OVERWRITE_PROMPT)
  if SaveDialog.ShowModal() == wx.ID_OK:
    Directory = SaveDialog.GetDirectory()
    FileName = SaveDialog.GetFilename()
    if FileName.split(".")[-1] != Format:
      FileName = FileName + "." + Format
    SaveBinary(Directory, FileName, Frame)
  SaveDialog.Destroy()


def SaveBinary (Directory, FileName, Frame):
  import urllib
  SongPath = "file:///home/puneeth/astute-song-hunter/client/saves/nin_2.wav"
  try :
    SongFile = open(Directory+"/"+FileName, "wb")
  except IOError:
    DisplayError("File cannnot be open!")
    return
  try:
    Song = urllib.urlopen(SongPath)
  except IOError:
    DisplayError("Invalid Server Path!")
    return
  SongFile.writelines(Song.read())
  SongFile.close()
  Dialog = wx.MessageDialog(None, "Song saved successfully at\n"+Directory, 'Songs Saved', wx.OK | wx.ICON_INFORMATION)
  Dialog.ShowModal()


def DisplayError(ErrorMessage):
  Dialog = wx.MessageDialog(None, ErrorMessage, 'Error!', wx.OK | wx.ICON_ERROR)
  Dialog.ShowModal()
