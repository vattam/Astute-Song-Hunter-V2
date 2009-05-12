import tkSnack, Tkinter

def play (Frame):
  ASH_Frame = Frame
  ASH_Sound = tkSnack.Sound(load="saves/.temp.wav")
  ASH_Frame.Tune.TkRoot.geometry("+200+200")
  
  Wave = tkSnack.SnackCanvas(height=200, width=400)
  Wave.pack()
  Wave.create_waveform(0, 0, sound=ASH_Sound, height=200, width=400)
  
  ASH_Sound.play()
  ASH_Frame.Tune.TkRoot.mainloop()
