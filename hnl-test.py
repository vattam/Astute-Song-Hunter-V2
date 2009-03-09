import line
import tkSnack, Tkinter

def HNL(c):
    (UP,DOWN,NUTRAL) = (1000, -1000, 0)
    APPROX = 3
    i = 0
    while c[i] == 0:
      i += 1
    c = c[i:]
    x = [UP]
    i = 1
    while i < len(c):
      v = c[i] - c[i-1]
      if abs(v) <= APPROX:
        x.append(NUTRAL)
      elif v < 0 :
        x.append(DOWN)
      else:
        x.append(UP)
      i += 1
    return x

def main():
    root = Tkinter.Tk()
    tkSnack.initializeSnack(root)
    Snd1 = tkSnack.Sound(load="songs/origkoikahe.wav")
    Snd2 = tkSnack.Sound(load="tunes/mkoi.wav")
    Y1 = HNL(Snd1.dBPowerSpectrum(fftlength=16384))
    Ang1 = line.normalize(Y1)
    
    Y2 = HNL(Snd2.dBPowerSpectrum(fftlength=16384))
    Ang2 = line.normalize(Y2)
    print Y1, Y2
    print line.angle(Ang1, Ang2)
    

if __name__ == "__main__":
    main()
