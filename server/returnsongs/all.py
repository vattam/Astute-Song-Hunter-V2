import tkSnack, Tkinter
import line
import os, wave
import audioop as Audio


class ConstructTags(tkSnack.Sound):
    def __init__(self, Song=None):
        tkSnack.Sound.__init__(self,load=Song)
        self.Length = None
        self.sampling_rate = None
        self.Stream = None

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

    def get_minmax_tag(self):
        min_list = []
        max_list = []
        i = 0
        while i <= self.Length :
            min_val, max_val = Audio.minmax(self.Stream[i:i+256], 1)
            min_list.append(min_val)
            max_list.append(max_val)
            i += 256
        return min_list, max_list

    def get_tags(self):
        spectrum = self.dBPowerSpectrum(fftlength=16384)
        slope = line.normalize(spectrum)
        min_list, max_list = self.get_minmax_tag()
        return (slope, max_list, min_list)


def main(path):
    Tags=[]
    root = Tkinter.Tk()
    tkSnack.initializeSnack(root)
    Song = ConstructTags()
    for Song_Name in os.listdir(path):
        Song_Path = path+Song_Name
        Song.load(Song_Path)
        Slope, max_list, min_list = Song.get_tags()
        Tags.append({"Name":Song_Name, "Path":Song_Path, "Slope":Slope, "MaxList":max_list, "MinList":min_list))

#    print len(Tags)
    return Tags
