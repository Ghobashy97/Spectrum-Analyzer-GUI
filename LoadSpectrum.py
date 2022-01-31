import scipy as sp
import numpy as np
from tkinter import *
from tkinter import filedialog
from tkinter.simpledialog import SimpleDialog
import librosa as lr
import audioread as aur


filetypesSpectrum=(
    ('text files', '*.txt'),
    ('data files', '*.dat'),
    ('ASCII files', '*.asc')
)

class LoadSpectrum:
    def __init__(self) -> None:
        pass

    def load_spectrum_file():
        global input_spectrum_object
        spectrum_path = filedialog.askopenfilename(filetypes=filetypesSpectrum)
        input_spectrum_object = np.load(spectrum_path)
        
        return None

    def do_ifft(spectrum_in):
        pass
