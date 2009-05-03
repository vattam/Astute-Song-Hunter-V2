from tkSnack import SnackCanvas
import Tkinter

ASH_Frame = None

def recorder (Frame):
  global ASH_Frame
  ASH_Frame = Frame
  Wave = SnackCanvas(height=200, width=200)
  Wave.pack()
  Wave.create_section(0, 0, sound=Frame.Tune.SnackSound, height=200, width=200)
  Tkinter.Button(Frame.Tune.TkRoot, bitmap='snackStop', command=stop).pack(side='left')
  Tkinter.Button(Frame.Tune.TkRoot, bitmap='snackRecord', fg='red', command=record).pack(side='right')
  ASH_Frame.Tune.TkRoot.mainloop()

def record():
  global ASH_Frame
  ASH_Frame.Tune.SnackSound.record()

def stop():
  global ASH_Frame
  ASH_Frame.Tune.SnackSound.stop()
  ASH_Frame.Tune.TkRoot.destroy()
  ASH_Frame.Tune.TkRoot = Tkinter.root()
