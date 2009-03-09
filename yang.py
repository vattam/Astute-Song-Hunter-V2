import wave, math
import audioop as Audio

def normalize(L,I):
  M = []
  j = 0
  for i in I:
    M.append((i-L[j])**2)
    j += 1
  return (sum(M)/len(M))**-1

Song1 = "../song/nin_1.wav"
Song2 = "../song/a.wav"

Song = wave.open(Song1,'rb')
Frame_Rate = Song.getframerate()
Num_Channels = Song.getnchannels()
Num_Frames = Song.getnframes()
Buffer = Num_Frames/256
Min1 = []
Max1 = []
Stream = Song.readframes(Buffer)
while len(Stream):
  Stream = Audio.lin2lin(Stream,2,1)
  if Num_Channels == 2:
    Stream = Audio.tomono(Stream,1,1,-1)
  a,b = Audio.minmax(Stream,1)
  Min1.append(a)
  Max1.append(b)
  Stream = Song.readframes(Buffer)
Song.close()

Song = wave.open(Song2,'rb')
Frame_Rate = Song.getframerate()
Num_Channels = Song.getnchannels()
Num_Frames = Song.getnframes()
Buffer = Num_Frames/256
Min2 = []
Max2 = []
Stream = Song.readframes(Buffer)
while len(Stream):
  Stream = Audio.lin2lin(Stream,2,1)
  if Num_Channels == 2:
    Stream = Audio.tomono(Stream,1,1,-1)
  a,b = Audio.minmax(Stream,1)
  Min2.append(a)
  Max2.append(b)
  Stream = Song.readframes(Buffer)
Song.close()

a = normalize(Max1,Max2)
b = normalize(Min1,Min2)
if abs(a-b) < 0.00005:
  print "The songs ",Song1," and ",Song2," are alomst same."
elif abs(a-b) >= 0.0001:
  print "The songs ",Song1," and ",Song2," are different."
else:
  print "The songs ",Song1," and ",Song2," are some what similar."
