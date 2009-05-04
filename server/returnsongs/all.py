import tkSnack, Tkinter
import line
import os, wave
import audioop as Audio


class ConstructTags(tkSnack.Sound):
    def __init__(self, Song=None):
        tkSnack.Sound.__init__(self,load=Song)
        self.Length = None
        self.sampling_rate = None

    def load(self,Song):
        self.read(Song)
        self.configure(channels=1)#, frequency=22050, fileformat='WAV', encoding='Lin8')
        self.Length = self.length(unit="SAMPLES")
        self.sampling_rate = self.cget("frequency")
        self.write("temp.wav")
        Temp = wave.open("temp.wav","rb")
        self.Stream = Temp.readframes(self.Length)
        Temp.close()
        os.remove("temp.wav")

    def get_minmax_tag(self, tag_start, tag_end):
        framebuffer = (tag_end-tag_start) / 256
        stream = self.Stream[tag_start:tag_end]
        min_list = []
        max_list = []
        while len(stream):
            min_val, max_val = Audio.minmax(stream[:256], 1)
            min_list.append(min_val)
            max_list.append(max_val)
            stream = stream[256:]
        return min_list, max_list


    def get_tags(self):
        num_tags = (self.Length / (self.sampling_rate * 5))
        dbpowerspectrum_tags_list = []
        max_tags_list = []
        min_tags_list = []
        
        for i in range (num_tags):
            tag_start = i * (self.sampling_rate * 5)
            tag_end = tag_start + self.tag_length
            if  tag_end > self.Length:
                tag_end = self.Length - 1
            spectrum = self.dBPowerSpectrum(fftlength=16384, start=tag_start, end=tag_end)
            dbpowerspectrum_tags_list.append(line.normalize(spectrum))
            min_list, max_list = self.get_minmax_tag(tag_start, tag_end)
            min_tags_list.append(min_list)
            max_tags_list.append(max_list)
        
        return (dbpowerspectrum_tags_list, max_tags_list, min_tags_list)


def main(path):
    Tags=[]
    root = Tkinter.Tk()
    tkSnack.initializeSnack(root)
    Song = ConstructTags()
    
    for Song_Name in os.listdir(path):
        Song_Name = path+Song_Name
        Song.load(Song_Name)
        dbspectrum,max_tags_list,min_tags_list = Song.get_tags()
        Tags.append((Song_Name,dbspectrum,(max_tags_list,min_tags_list)))
        print Song_Name
    
    return Tags


if __name__ == "__main__":
    main()
