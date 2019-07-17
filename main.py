import numpy as np
import scipy.io.wavfile as wavfile
from scipy import fftpack
import matplotlib.pyplot as plt

rate, data = wavfile.read("Sounds/6thE.wav")
plt.rcParams['figure.figsize'] = 16, 8


fs = 44100
ts = 1/fs

data = data.T[1]
fft_out = fftpack.fft(data)
power = np.abs(fft_out)
sample_freq = fftpack.fftfreq(fft_out.size, d=ts)
half = int(len(sample_freq)/2)

peak_freq = sample_freq[power.argmax()]
print(peak_freq)

plt.xlabel('Frequency [Hz]')
plt.ylabel('Power')
plt.plot(sample_freq[:half], power[:half]*1/len(power))
plt.grid()
plt.show()
