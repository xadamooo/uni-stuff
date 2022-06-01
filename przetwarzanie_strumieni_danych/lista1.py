import numpy as np
import scipy.signal as sig
from scipy.io import wavfile
import matplotlib.pyplot as plt
import random


klarnet_path = 'D:\\PWR\\Visual Studio\\przetwarzanie_strumieni_danych\\sounds\\klarnet.wav'



def fft1(x):
    if len(x) == 2:
        return np.array([x[0] + x[1], x[0] - x[1]], dtype=np.complex128)
    even = fft1(x[::2])
    odd = fft1(x[1::2])
    w = np.exp(-2 * np.pi * 1j * np.arange(len(x) // 2) / len(x))
    X = np.hstack((even + w * odd, even - w * odd))
    return X


sampling_frequency = 48000
hz1 = 100
n = np.arange(2048)
sine = np.sin(2 * np.pi * n * hz1 / sampling_frequency)
print('Własna funkcja FFT:')
print(fft1(sine))
print('Numpy FFT:')
print(np.fft.fft(sine))


spectrum = np.fft.fft(sine)


hz1 = 100
hz2 = 300
hz3 = 500
f = np.fft.rfftfreq(len(n), 1 / sampling_frequency)
mixed_sin = (np.sin(2 * np.pi * n * hz1 / sampling_frequency) +
             np.sin(2 * np.pi * n * hz2 / sampling_frequency) +
             np.sin(2 * np.pi * n * hz3 / sampling_frequency))


spectr_amp = np.abs(np.fft.rfft(sine)) / 1024
f = np.fft.rfftfreq(2048, 1/sampling_frequency)
plt.plot(f, spectr_amp)
plt.xlabel('częstotliwość [Hz]')
plt.ylabel('amplituda')
plt.title('Widmo amplitudowe sygnału sinusoidalnego 0.1 kHz')
plt.show()


spectr_mixed_sin = np.fft.rfft(mixed_sin)
plt.plot(f, np.abs(spectr_mixed_sin) / 1024)
plt.xlim(0, 5000)
plt.xlabel('częstotliwość [Hz]')
plt.ylabel('amplituda')
plt.title('Widmo amplitudowe zmieszanego sygnału trzech sinusów')
plt.show()


plt.plot(f, 20 * np.log10(np.abs(spectr_amp) / 1024))
plt.xlim(0, 5000)
plt.xlabel('częstotliwość [Hz]')
plt.ylabel('amplituda')
plt.title('Widmo amplitudowe sygnału sinusoidalnego 0.1kHz - skala decybelowa')
plt.show()


plt.plot(f, 20 * np.log10(np.abs(spectr_mixed_sin) / 1024))
plt.xlim(0, 5000)
plt.xlabel('częstotliwość [Hz]')
plt.ylabel('amplituda')
plt.title('Widmo amplitudowe zmieszanego sygnału trzech sinusów - skala decybelowa')
plt.show()


f, t, Sxx = sig.spectrogram(sine)
plt.pcolormesh(t, f, 20 * np.log10(Sxx), shading='auto')
plt.xlabel('czas')
plt.ylabel('częstotliwość [Hz]')
plt.title('Spektrogram sygnalu 100Hz')
plt.colorbar()
plt.show()


f, t, Sxx = sig.spectrogram(mixed_sin)
plt.pcolormesh(t, f, 20 * np.log10(Sxx), shading='auto')
plt.xlabel('czas [s]')
plt.ylabel('częstotliwość [Hz]')
plt.title('Spektrogram sygnalu zmieszanego')
plt.colorbar()
plt.show()


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


wav_fs, clarnet = wavfile.read(klarnet_path)
f, t, Sxx = sig.spectrogram(clarnet, fs=wav_fs, window=np.hamming(2048), nperseg=2048, noverlap=1500,
                            scaling='density', mode='magnitude')
plt.figure(figsize=(16, 8))
plt.pcolormesh(t, f, 20 * np.log10(Sxx), shading='auto')
plt.xlabel('czas')
plt.ylabel('częstotliwość [Hz]')
plt.title('Spektrogram klarnetu')
plt.ylim(0, 8000)
plt.colorbar()
plt.show()


t = np.linspace(2, 5000, 1000)
chirp = sig.chirp(t, 20, 1, 5000, 'linear')
b, a = sig.butter(1, [0.1, 0.9], btype='band')
filtered = sig.filtfilt(b, a, chirp)
plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.plot(chirp)
plt.title("Sygnał Chirp")
plt.subplot(122)
plt.plot(filtered)
plt.title("Przefiltrowany sygnał Chirp z użyciem SciPy")
plt.tight_layout()
plt.show()


filtr = chirp.copy()
filtered = np.fft.rfft(filtr)
for k in range(len(filtered)):
    if filtered[k] < 0.1 or filtered[k] > 0.9:
        filtered[k] = 0
    else:
        filtered[k] /= 100
inverse_chirp = np.fft.ifft(filtered, n=1000, norm='forward')
plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.plot(chirp)
plt.title("Chirp signal")
plt.subplot(122)
plt.plot(inverse_chirp[1:])
plt.title("Przefiltrowany sygnał Chirp z użyciem algorytmu IFFT")
plt.tight_layout()
plt.show()
