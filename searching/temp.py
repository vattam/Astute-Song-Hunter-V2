import tkSnack, Tkinter
import wave,audioop
import os, time
from search import *

def get_data():
#    MySound.configure(channels=1, frequency=22050, fileformat='WAV', encoding='Lin8')
    T.calculate_slope(MySound.dBPowerSpectrum(fftlength=16384))
    MySound.write("temp.wav")
    S = wave.open("temp.wav","rb")
    N = MySound.length(unit="SAMPLES")
    Stream = S.readframes(N)
    S.close()
    os.remove("temp.wav")
    T.calculate_max_min(Stream,N)


def search():
    Match1 = search_by_regression(T.Slope)
    Match2 = search_by_max_min(T.Max_List, T.Min_List)
    print "The relatively matched songs are : "
    print Match1
    print Match2
    for i in Match1:
      if i in Match2:
        print i


class Tag:
  def __init__(self):
    self.Max_List = []
    self.Min_List = []
    self.Slope = None
  
  def calculate_max_min(self,Stream,Length):
    Frame_Buffer = Length / 256
    i = 0
    while i <= Length:
      min_val, max_val = audioop.minmax(Stream[i:i+256], 1)
      self.Min_List.append(min_val)
      self.Max_List.append(max_val)
      i += 256
  
  def calculate_slope(self,L):
    I = [i for i in range(1,len(L)+1)]
    II = [i*i for i in I]
    IL = []
    for i in I:
      IL.append(i*L[i-1])
    self.Slope = (len(I)*sum(IL) - sum(I)*sum(L)) / (len(I)*sum(II) - sum(I)*sum(I))


root = Tkinter.Tk()
tkSnack.initializeSnack(root)
MySound = tkSnack.Sound(load="../tunes/nin_2.wav")
T = Tag()
get_data()
t = time.time()
search()
print "Time to search is : ",time.time()-t,"seconds."
