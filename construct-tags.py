import tkSnack, Tkinter
import line
import math
import wave
import os
import audioop as Audio



class ConstructTags(object):
    def __init__(self, SongSnack, SongWave):
        self.SongSnack = SongSnack
        self.SongWave = SongWave
        (self.length, self.sampling_rate, self.max_val, self.min_val, self.encoding,
            self.num_channels, self.fileFormat, self.headerSize) = self.SongSnack.info()
        self.sample_width = self.SongWave.getsampwidth()
    
    def get_minmax_tag(self, tag_stream, num_frames):
        buffer_song = wave.open('temp_buf', 'wb')
        buffer_song.setnchannels(self.num_channels)
        buffer_song.setframerate(self.sampling_rate)
        buffer_song.setsampwidth(self.sample_width)
        buffer_song.writeframesraw(tag_stream)
        buffer_song.close()

        buffer_song = wave.open('temp_buf', 'rb')
        
        framebuffer = num_frames / 256
        stream = buffer_song.readframes(framebuffer)
        min_list = []
        max_list = []
        while len(stream):
            stream = Audio.lin2lin(stream, 2, 1)
            if self.num_channels == 2:
                stream = Audio.tomono(stream, 1, 1, -1)
            min_val, max_val = Audio.minmax(stream, 1)
            min_list.append(min_val)
            max_list.append(max_val)
            stream = buffer_song.readframes(framebuffer)

        buffer_song.close()
        os.remove('temp_buf')
        return min_list, max_list


    def get_tags(self):        
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
            stream = self.SongWave.readframes(tag_end - tag_start)
            min_list, max_list = self.get_minmax_tag(stream, tag_end - tag_start)
            min_tags_list.append(min_list)
            max_tags_list.append(max_list)

        return (dbpowerspectrum_tags_list, max_tags_list, min_tags_list)

def main():
    root = Tkinter.Tk()
    tkSnack.initializeSnack(root)
    Snd1 = tkSnack.Sound(load="songs/origguzarish-ghajini.wav")
#    Snd2 = tkSnack.Sound(load="tunes/ghajini.wav")
    SongWave1 = wave.open("songs/origguzarish-ghajini.wav",'rb')
    contag = ConstructTags(Snd1, SongWave1)
    contag.get_tags()
    SongWave1.close()
    
if __name__ == "__main__":
    main()
