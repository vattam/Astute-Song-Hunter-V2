import wx
import time

class SplashScreen(wx.Frame): 
  def __init__(self,ClientFrame):
    self.ClientFrame = ClientFrame
    wx.Frame.__init__(self,None, -1,size=(500,344), style=wx.FRAME_NO_TASKBAR | wx.FRAME_EX_METAL)
    Img = wx.Image('icons/splash.jpg',wx.BITMAP_TYPE_JPEG)
    wx.StaticBitmap(self,-1, Img.ConvertToBitmap())
    self.Timer = wx.Timer(None, -1)
    self.Timer.Bind(wx.EVT_TIMER, self.endScreen)
    self.Timer.Start(milliseconds=3000, oneShot=True)
    self.Show(True)
    self.Center()

  def endScreen(self, event): 
    self.Close()
    self.ClientFrame.Show(True)
