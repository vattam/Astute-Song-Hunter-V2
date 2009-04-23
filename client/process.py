import audioop
import wave
import os

class Tag:
  def __init__(self, Sound):
    self.Max_List = []
    self.Min_List = []
    self.Slope = None
    self.Sound = Sound

  def calculate_max_min(self):
    self.Sound.write(".temp.wav")
    S = wave.open(".temp.wav","rb")
    Length = self.Sound.length(unit="SAMPLES")
    Stream = S.readframes(Length)
    S.close()
    os.remove(".temp.wav")
    Frame_Buffer = Length / 256
    i = 0
    while i <= Length:
      min_val, max_val = audioop.minmax(Stream[i:i+256], 1)
      self.Min_List.append(min_val)
      self.Max_List.append(max_val)
      i += 256

  def calculate_slope(self):
    L = self.Sound.dBPowerSpectrum(fftlength=16384)
    I = [i for i in range(1,len(L)+1)]
    II = [i*i for i in I]
    IL = []
    for i in I:
      IL.append(i*L[i-1])
    self.Slope = (len(I)*sum(IL) - sum(I)*sum(L)) / (len(I)*sum(II) - sum(I)*sum(I))

