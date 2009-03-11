import tkSnack, Tkinter
import line
import os, wave, time
import audioop as Audio

class ConstructTags(tkSnack.Sound):
    def __init__(self, Song=None):
        tkSnack.Sound.__init__(self,load=Song)
        self.tag_length = 22050 * 20
        self.Length = 0
        self.sampling_rate = 22050

    def load(self,Song):
        self.read(Song)
        self.configure(channels=1, frequency=22050, fileformat='WAV', encoding='Lin8')
        self.Length = self.length(unit="SAMPLES")
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

def main():
    root = Tkinter.Tk()
    tkSnack.initializeSnack(root)
    Song_Name = "songs/milana1.mp3"
    Song = ConstructTags()
    t1 = time.time()
    Song.load(Song_Name)
    dbpowerspectrum,max_tags_list,min_tags_list = Song.get_tags()
    print "Time to extract the tags is : ",time.time()-t1,"seconds"
    print "Size of Meta Data kept is :",len(dbpowerspectrum)*4+len(max_tags_list)*len(max_tags_list[1])*2*2,"bytes"

if __name__ == "__main__":
    main()
