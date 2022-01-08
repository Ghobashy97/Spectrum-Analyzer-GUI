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
from tkinter import *
import matplotlib.pyplot as pplt
import matplotlib as plt


####################  Structure of the GUI   ######################

root = Tk()
root.title("Spectrum Analyzer")
#................inputs.................................................................

def browseButtonClick():
    data_from_read_file = 123
    read_file_type = ".wav file"
    file_read_status = Label(root, text= read_file_type, fg="yellow", bg="black")
    file_read_status.grid(row=3, column=0)

browseButton = Button(root, text="Browse for sound file", fg="yellow", bg="black", command=browseButtonClick,padx=5,pady=5)
browseButton.grid(row=2,column=0)



#............Classes for S(t) and S(f)..................................................


class waveformPlot:
    def __init__(self,s_t_name, t_size, s_t):
        self.s_t_name = s_t_name
        self.t_size = t_size
        self.s_t = s_t
    
    
class spectrumPlot:
    def __init__(self,s_f_name,f_size, s_f):
        self.s_f_name = s_f_name
        self.f_size = f_size
        self.s_f = s_f

#.............fourier analysis...........................................................





#............mainloop....................................................................
root.mainloop()