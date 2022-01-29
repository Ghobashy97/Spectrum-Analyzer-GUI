from logging import root
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from SignalManipulation import SignalData
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


        def radio_changed():
            current_radio = selected.get()
            if current_radio == 2:
                openwav.grid(row=2, column=2)
                # expinput.grid_remove()
                opendat.grid_remove()

            elif current_radio == 3:
                openwav.grid_remove()
                # expinput.grid_remove()
                opendat.grid(row=2, column=3)
        def load_wav_file():
            file_signal_data = filedialog.askopenfile(filetypes=filetypesSignal)
            input_signal_object = SignalData(inp_sig=file_signal_data, 
                                            t_len=len(file_signal_data))
            return None

        def load_spectrum_file():
            file_spectrum_data = filedialog.askopenfile(filetypes=filetypesSpectrum)
            input_spectrum_object = SignalData(file_spectrum_data)

            return None
        
                



        openwav = Button(root, text="Open .wav File", bg="#474848", fg="white", 
                        command = load_wav_file, pady=10, padx=10)
        opendat = Button(root, text="Open .DAT File", bg="#474848", fg="white",
                        command=load_spectrum_file, pady=10,padx=10)

        selected = IntVar()

        rad2 = Radiobutton(root,text='Import .wav file', value=2, 
                          variable=selected, padx=30, pady= 15,
                           command=radio_changed)
        rad3 = Radiobutton(root,text='Import Spectrum Data', value=3,
                          variable=selected, padx=30, pady=15,
                           command=radio_changed)

        # rad1.grid(row=1, column=1)
        rad2.grid(row=1, column=2)
        rad3.grid(row=1, column=3)

        root.mainloop()

    creat_gui_elements()





    
