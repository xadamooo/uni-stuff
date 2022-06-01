import numpy as np
import scipy.signal as sig
from scipy.io import wavfile
import matplotlib.pyplot as plt
import random


sampling_frequency = 48000
chirp = sig.chirp(np.arange(sampling_frequency) / sampling_frequency, 20, 1, 5000, 'linear')
f, t, Sxx = sig.spectrogram(chirp, fs=sampling_frequency, window=np.hamming(2048), nperseg=2048, noverlap=1500,
                            scaling='density', mode='magnitude')
plt.pcolormesh(t, f, 20 * np.log10(Sxx), shading='auto')
plt.xlabel('czas [s]')
plt.ylabel('częstotliwość [Hz]')
plt.title('Spektrogram sygnału chirp')
plt.ylim(0, 5000)
plt.colorbar()
plt.show()