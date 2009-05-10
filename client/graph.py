import wx, os
import wx.lib.plot as plot
import Tkinter

def GraphDisplay (Data):
  Frame = wx.Frame(None)
  Panel1 = wx.Panel(Frame)
  Plotter = plot.PlotCanvas(Panel1)
  Plotter.SetSize((270,200))
  Line = plot.PolyLine(Data, colour='grey', width=2)
  Marker = plot.PolyMarker(Data, marker='dot')
  GraphCanvas = plot.PlotGraphics([Line, Marker])
  Plotter.SetFontSizeAxis(point=0)
  Plotter.Draw(GraphCanvas)
  Plotter.SaveFile(".wave.jpg")
  Frame.Destroy()


def GetGraph():
  File = open(".image.ps","r")
  List = File.readlines()[332:1132]
  File.close()
  Data = []
  for i in List:
    i = i.split(" ")
    Data.append((float(i[0]),float(i[1])))
  GraphDisplay(Data)
