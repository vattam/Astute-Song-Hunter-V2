import tkSnack, Tkinter
import line,math


import wave
import audioop as Audio


Stream = Song.readframes(Buffer)
print Stream

class ConstructTags(object):
    def __init__(SongSnack, SongWave):
        self.SongSnack = SongSnack
        self.SongWave = SongWave
        (self.length, self.sampling_rate, self.max_val, self.min_val, self.encoding,
            self.channels, self.fileFormat, self.headerSize = self.SongSnack.info()
    
    def get_minmax_tag(stream, num_frames, num_channels):
        framebuffer = num_frames/256
        min_list = []
        max_list = []
        while len(stream):
            stream = Audio.lin2lin(stream, 2, 1)
            if Num_Channels == 2:
                stream = Audio.tomono(stream, 1, 1, -1)
            min_val, max_val = Audio.minmax(stream, 1)
            min_list.append(min_val)
            max_list.append(max_val)
            stream = Song.readframes(framebuffer)
        
        return min_list, max_list


    def get_tags():        
        tag_length = self.sampling_rate * 20
        num_tags = (self.length / (self.sampling_rate * 5))
        dbpowerspectrum_tags_list = []
        max_tags_list = []
        min_tags_list = []
        
        for i in range (num_tags):
            tag_start = i * (self.sampling_rate * 5)
            tag_end = tag_start + tag_length
            if  tag_end > self.length:
                tag_end = self.length - 1
            dbpowerspectrum_tags_list.append(self.SongSnack.dBPowerSpectrum(fftlength=16384,
                start=tag_start, end=tag_end))
            stream = Song.readframes(tag_end - tag_start)
            min_list, max_list = self.get_minmax_tag(stream, num_frames, num_channels)
            min_tags_list.append(min_list)
            max_tags_list.append(max_list)

        return (dbpowerspectrum_tags_list, max_tags_list, min_tags_list)

def main():
    root = Tkinter.Tk()
    tkSnack.initializeSnack(root)
    Snd1 = tkSnack.Sound(load="songs/milana1.wav")
    Snd2 = tkSnack.Sound(load="tunes/ghajini.wav")
    SongWave1 = wave.open("songs/origguzarish-ghajini.wav",'rb')
    contag = ConstructTags(Snd1, SongWave1)
    contag.get_tags()

if __name__ == "__main__":
    main()
