from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.simpledialog import SimpleDialog
from SignalManipulation import SignalData
from Plotting import DataPlotDisplay
from scipy.io.wavfile import read, write
import librosa as lr

# from Plotting import .....

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


class SpectrumAnalyzerGUI:
    def __init__(self) -> None:
        pass

    def creat_gui_elements():
        global root 
        root= Tk()

        root.title("Spectrum Analyzer")
        root.geometry('1280x720')
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

        def load_wav_file():
            global input_signal_object, f_s
            audio_path = filedialog.askopenfilename(filetypes=filetypesSignal)            
            loaded_signal_data, f_s = lr.load(audio_path)
            input_signal_object = SignalData(inp_sig=loaded_signal_data, 
                                            f_samp=f_s)
            print(loaded_signal_data)
            return None

        def load_spectrum_file():
            global input_spectrum_object
            file_spectrum_data = filedialog.askopenfilename(filetypes=
                                                       filetypesSpectrum)

            input_spectrum_object = SignalData(file_spectrum_data)

            return None
        
                

        panel1 = PanedWindow(orient=HORIZONTAL)
        panel1.pack(side=TOP)

        panel2 = PanedWindow(orient=HORIZONTAL)
        panel2.pack(side=TOP)
        
        


        openwav = Button(panel2, text="Open Sound File", bg="#474848",  
                        fg="white",command = load_wav_file, pady=10, padx=10)
        
        opendat = Button(panel2, text="Open Spectrum File", bg="#474848", 
                        fg="white",command=load_spectrum_file, pady=10,padx=10)
        

        selected = IntVar()
        rad2 = Radiobutton(panel1,text='Import .wav file', value=2, 
                            variable=selected, padx=30, pady= 15,
                            command=radio_changed)

        rad3 = Radiobutton(panel1,text='Import Spectrum Data', value=3,
                            variable=selected, padx=30, pady=15,
                            command=radio_changed)

        # rad1.grid(row=1, column=1)
        rad2.pack(side=LEFT)
        rad3.pack(side=RIGHT)

        root.mainloop()

    creat_gui_elements()





    
