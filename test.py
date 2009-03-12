import line,os,time
import tkSnack, Tkinter

def HNL(c):
    (UP,DOWN,NUTRAL) = ('H','L','N')
    APPROX = 5
    i = 0
    while c[i] == 0:
      i += 1
    c = c[i:]
    x = UP
    i = 1
    while i < len(c):
      v = c[i] - c[i-1]
      if abs(v) <= APPROX:
        x += NUTRAL
      elif v < 0 :
        x += DOWN
      else:
        x += UP
      i += 1
    return x

def match(Tune):
    root = Tkinter.Tk()
    tkSnack.initializeSnack(root)
    t = 0
    t1 = time.time()
    Snd1 = tkSnack.Sound(load=Tune)
    Y1 = Snd1.dBPowerSpectrum(fftlength=16384)
    Ang1 = line.normalize(Y1)
    t += time.time()-t1
    Snd2 = tkSnack.Sound()
    M = []

    for Tag in os.listdir("songs"):
      Snd2.read("songs/"+Tag)
      Y2 = Snd2.dBPowerSpectrum(fftlength=16384)
      Ang2 = line.normalize(Y2)
      t1 = time.time()
      if line.angle(Ang1, Ang2) < 5e-03:
        M.append(Tag)
      t += time.time()-t1
    return t,M

