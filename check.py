import wave, math
import audioop as Audio
import line
import os,sys

Tune = "tunes/"+sys.argv[1]

Song = wave.open(Tune,'rb')
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

print "The relative match for '",Tune,"' are : "

for Tag in os.listdir("songs"):
  Song = wave.open("songs/"+Tag,'rb')
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
  a = line.rms(Max1,Max2)
  b = line.rms(Min2,Min1)
  diff = int(abs(a-b)*(10**5))
  if diff < 5:
    print Tag," - ",diff
