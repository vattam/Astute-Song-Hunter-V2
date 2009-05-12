import tkSnack
import Tkinter

ASH_Frame = None
ASH_Sound = None
IS_RECORDED = False

def recorder (Frame):
  global ASH_Frame, ASH_Sound
  ASH_Frame = Frame
  ASH_Sound = tkSnack.Sound()
  ASH_Frame.Tune.TkRoot.geometry("+100+100")
  Wave = tkSnack.SnackCanvas(height=200, width=400)
  Wave.pack()
  Wave.create_waveform(0, 0, sound=ASH_Sound, height=200, width=400)
  Tkinter.Button(Frame.Tune.TkRoot, bitmap='snackStop', command=stop).pack(side='left')
  Tkinter.Button(Frame.Tune.TkRoot, bitmap='snackRecord', fg='red', command=record).pack(side='right')
  ASH_Frame.Tune.TkRoot.mainloop()

def record():
  global ASH_Frame, ASH_Sound, IS_RECORDED
  IS_RECORDED = True
  ASH_Sound.record()

def stop():
  global ASH_Frame, ASH_Sound, IS_RECORDED
  if IS_RECORDED == False:
    return
  ASH_Sound.stop()
  ASH_Sound.write("saves/.temp.wav")
  ASH_Frame.Tune.TkRoot.destroy()
