# Spectrum Analyzer by Aly M. Ghobashy (C) 2022
# https://twitter.com/GebzNotJebz
# https://github.com/Ghobashy97
#
#
#

#.............Libraries and Dependancies...............................................

import scipy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as pplt
import matplotlib as plt
import wave as wv
from scipy.io import wavfile

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

import waveform as wf
import spectrum as sp



####################  Structure of the GUI   ######################

root = Tk()
root.title("Spectrum Analyzer")

#................inputs.................................................................
#...............Reading the .wav Data...................................................



openwav = Button(root, text = "Open .wav File", bg = "black", fg = "Yellow", command = filedialog.askopenfilenames, pady=10, padx=10)
expinput = Entry(root,width=50, borderwidth=5)
opendat = Button(root, text="Open .DAT File", bg= "black",fg = "Yellow", command = filedialog.askopenfilenames, pady=10, padx=10)


def radio_changed():
    current_radio = selected.get()
    if (current_radio==2):
        openwav.grid(row=2, column=2)
        expinput.grid_remove()
        opendat.grid_remove()
    elif (current_radio==1):
        openwav.grid_remove()
        opendat.grid_remove()
        expinput.grid(row=2, column=1, padx=20, pady=10)
    elif (current_radio==3):
        openwav.grid_remove()
        expinput.grid_remove()
        opendat.grid(row=2, column=3)

    


selected = IntVar()
rad1 = Radiobutton(root,text='Enter Analytical Expression', value=1, variable=selected, padx=30, pady= 15, command=radio_changed)
rad2 = Radiobutton(root,text='Import .wav file', value=2, variable=selected, padx=30, pady= 15, command=radio_changed)
rad3 = Radiobutton(root,text='Import Spectrum Data', value=3, variable=selected, padx=30, pady= 15, command=radio_changed)

rad1.grid(row=1, column=1)
rad2.grid(row=1, column=2)
rad3.grid(row=1, column=3)





#............mainloop....................................................................
root.mainloop()