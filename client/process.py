import audioop
import wave
import os

class Tag:
  def __init__(self, Sound):
    self.Max_List = []
    self.Min_List = []
    self.Slope = None
    self.Sound = Sound
    self.Sound.configure(channels=1, fileformat='WAV', encoding='Lin8')
    self.FragmentFactor = 256

  def calculate_max_min(self):
    self.Sound.write(".temp.wav")
    S = wave.open(".temp.wav","rb")
    Length = S.getnframes()
    BufferLen = Length / self.FragmentFactor
    Stream = S.readframes(BufferLen)
    while len(Stream) :
      min_val, max_val = audioop.minmax(Stream, 1)
      self.Min_List.append(min_val)
      self.Max_List.append(max_val)
      Stream = S.readframes(BufferLen)
    S.close()
    os.remove(".temp.wav")

  def calculate_slope(self):
    L = self.Sound.dBPowerSpectrum(fftlength=16384)
    I = [i for i in range(1,len(L)+1)]
    II = [i*i for i in I]
    IL = []
    for i in I:
      IL.append(i*L[i-1])
    self.Slope = (len(I)*sum(IL) - sum(I)*sum(L)) / (len(I)*sum(II) - sum(I)*sum(I))

