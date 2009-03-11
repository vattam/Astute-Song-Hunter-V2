import wave, math
import audioop as Audio
import line

Song1 = "tunes/ghajini.wav"
Song2 = "songs/ghajini.wav"

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

print Max1
print Min1
a = line.rms(Max1,Max2)
b = line.rms(Min2,Min1)
print a,b

diff = int(abs(a-b)*(10**5))
print diff

if diff < 5:
  print "The songs ",Song1," and ",Song2," are alomst same."
elif diff >= 10:
  print "The songs ",Song1," and ",Song2," are different."
else:
  print "The songs ",Song1," and ",Song2," are some what similar."
