import numpy as np
import librosa as lr
import scipy as sp
import matplotlib as mpl
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.simpledialog import SimpleDialog
from tkinter.tix import Tree
from venv import create
from wave import Wave_read as wvrd
import audioread as aur
import audio2numpy as a2n


filetypesSound = (
    ('text files', '*.txt'),
    ('mp3 files', '*.mp3'),
    ('wav files', '*.wav'),
    ('data files', '*.dat'),
    ('ASCII files', '*.asc')
)


filetypesSpectrum = (
    ('text files', '*.txt'),
    ('data files', '*.dat'),
    ('ASCII files', '*.asc')
)


def plot_data():
    pass


def load_spectrum_file():
    global input_spectrum_object
    spectrum_path = filedialog.askopenfilename(filetypes=filetypesSpectrum)
    input_spectrum_object = np.load(spectrum_path)

    return None


def do_ifft(spectrum_in):
    pass


def load_sound_file():
    global signal_array, signal_fs
    audio_path = filedialog.askopenfilename(filetypes=filetypesSound)
    # print(audio_path)
    signal_array, signal_fs = a2n.audio_from_file(audio_path)

    try:
        signal_array = [signal_array[i][1] for i in range(len(signal_array))]
        #print(signal_array, signal_fs)
    except:
        print(123)

    def do_fft(signal_in, sample_rate):
        output_spectrum = []
        frequency_axis = [i for i in range(sample_rate)]

        return output_spectrum

    signal_transformed = do_fft(signal_array)
    

    return None


def create_gui_elements():

    root = Tk()

    root.title("Spectrum Analyzer")
    # root.geometry('1280x720')
    # root.call('wm', 'iconphoto', root._w,
    #          PhotoImage(file='Spectrum_Analyzer.png'))

    def radio_changed():
        current_radio = selected.get()
        if current_radio == 2:
            openwav.pack(side=TOP)
            # expinput.grid_remove()
            opendat.pack_forget()

        elif current_radio == 3:
            openwav.pack_forget()
            # expinput.grid_remove()
            opendat.pack(side=TOP)

    panel1 = PanedWindow(orient=HORIZONTAL)
    panel1.pack(side=TOP)

    panel2 = PanedWindow(orient=HORIZONTAL)
    panel2.pack(side=TOP)

    openwav = Button(panel2, text="Open Sound File", bg="#474848",
                     fg="white", command=load_sound_file, pady=10, padx=10)

    opendat = Button(panel2, text="Open Spectrum File", bg="#474848",
                     fg="white", command=load_spectrum_file, pady=10, padx=10)

    selected = IntVar()
    rad2 = Radiobutton(panel1, text='Import .wav file', value=2,
                       variable=selected, padx=30, pady=15,
                       command=radio_changed)

    rad3 = Radiobutton(panel1, text='Import Spectrum Data', value=3,
                       variable=selected, padx=30, pady=15,
                       command=radio_changed)

    rad2.pack(side=LEFT)
    rad3.pack(side=RIGHT)

    # gui_data_display()

    root.mainloop()


create_gui_elements()
