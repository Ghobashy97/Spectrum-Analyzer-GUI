from scipy import *
from numpy import *


class SignalData:
    def __init__(self, sig_name, inp_sig, inp_spect, out_wavfo, out_spectr, f_samp, t_len, freq_res):

        self.sig_name = sig_name
        self.inp_sig = inp_sig
        self.inp_spect = inp_spect
        self.out_wavfo = out_wavfo
        self.out_spectr = out_spectr
        self.f_samp = f_samp
        self.t_len = t_len
        self.freq_res = freq_res

        if (bool(inp_spect) == False) and (bool(inp_sig) == True):

            out_spectr = fft.fftshift(fft(inp_sig))

        elif (bool(inp_sig) == False) and (bool(inp_spect) == True):

            out_wavfo = ifft(fft.ifftshift(inp_spect))
