# Spectrum Analyzer by Aly M. Ghobashy (C) 2022
# https://twitter.com/GebzNotJebz
# https://github.com/Ghobashy97
#
#
#

#.............Libraries and Dependancies...............................................

from scipy import *
from numpy import *
from pandas import *
from matplotlib import*
from wave import *
from scipy.io import wavfile
from screeninfo import get_monitors

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox



# Root Tkinter window



root = Tk()
root.title("Spectrum Analyzer")
root.geometry('maximized')




# Accepted File Types

filetypesSignal = (
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




class signalData:
    def __init__(self,sig_name, inp_sig, inp_spect, out_wavfo, out_spectr, f_samp, t_len, freq_res):

        self.sig_name  = sig_name
        self.inp_sig = inp_sig
        self.inp_spect = inp_spect 
        self.out_wavfo = out_wavfo
        self.out_spectr = out_spectr
        self.f_samp = f_samp
        self.t_len  = t_len
        self.freq_res = freq_res 




        if (bool(inp_spect)==False) and (bool(inp_sig)==True):
               
            out_spectr = fft.fftshift(fft(inp_sig))
        
        elif (bool(inp_sig)==False) and (bool(inp_spect)==True):
            
            out_wavfo = ifft( fft.ifftshift(inp_spect))



def loadWavFile():
    
    global fileSignalData 
    fileSignalData = filedialog.askopenfile(filetypes=filetypesSignal)

    
    global input_signal_object
    input_signal_object = signalData(inp_sig=fileSignalData, t_len=len(fileSignalData))

    

    return None






def loadSpectrumFile():
    
    global fileSpectrumData 
    fileSpectrumData  = filedialog.askopenfile(filetypes=filetypesSpectrum)

    global input_spectrum_object
    input_spectrum_object = signalData(fileSpectrumData)

    return None




openwav = Button(root, text = "Open .wav File", bg = "#474848", fg = "white", command = loadWavFile, pady=10, padx=10)
#expinput = Entry(root,width=50, borderwidth=5)
opendat = Button(root, text="Open .DAT File", bg= "#474848",fg = "white", command = loadSpectrumFile, pady=10, padx=10)




def radio_changed():
    current_radio = selected.get()
    if (current_radio==2):
        openwav.grid(row=2, column=2)
        #expinput.grid_remove()
        opendat.grid_remove()

        
    #elif (current_radio==1):
    #    openwav.grid_remove()
    #    opendat.grid_remove()
    #    #expinput.grid(row=2, column=1, padx=20, pady=10)
    
    
    elif (current_radio==3):
        openwav.grid_remove()
        #expinput.grid_remove()
        opendat.grid(row=2, column=3)

    


selected = IntVar()
#rad1 = Radiobutton(root,text='Enter Analytical Expression', value=1, variable=selected, padx=30, pady= 15, command=radio_changed)
rad2 = Radiobutton(root,text='Import .wav file', value=2, variable=selected, padx=30, pady= 15, command=radio_changed)
rad3 = Radiobutton(root,text='Import Spectrum Data', value=3, variable=selected, padx=30, pady= 15, command=radio_changed)

#rad1.grid(row=1, column=1)
rad2.grid(row=1, column=2)
rad3.grid(row=1, column=3)





#............mainloop....................................................................
root.mainloop()