import scipy as sp
import numpy as np
from tkinter import *
from tkinter import filedialog
from tkinter.simpledialog import SimpleDialog
import librosa as lr
import audioread as aur



filetypesSound=(
    ('text files', '*.txt'),
    ('mp3 files', '*.mp3'),
    ('wav files', '*.wav'),
    ('data files', '*.dat'),
    ('ASCII files', '*.asc')
)


class LoadSound:
    def __init__(self) -> None:
        pass

    def load_sound_file():
            global input_signal_object, signal_array, signal_fs, signal_tlen, computed_spectrum
            audio_path = filedialog.askopenfilename(filetypes=filetypesSound)                    
            loaded_signal1= aur.audio_open(audio_path)                                   
            signal_array, signal_fs = lr.load(audio_path)                                      
            signal_fs = loaded_signal1.samplerate                                        
            signal_tlen = loaded_signal1.duration                                        
            
            print(signal_array, signal_fs, signal_tlen, signal_array)                  
            return None

    def do_fft(signal_in, sample_rate):
        output_spectrum=[]
        frequency_axis = [i for i in range(sample_rate)]

        return output_spectrum
