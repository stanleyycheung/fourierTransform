import numpy as np
import scipy.io.wavfile as wavfile
from scipy.fftpack import fft
import matplotlib.pyplot as plt

rate, data = wavfile.read("Sounds/6thE.wav")

data = data.T[0]
print(data)
plt.plot(data)
plt.xlabel(r'Time ($\mu s$)')
plt.grid()
plt.show()


# fft_out = fft(data)
# plt.plot(data, np.abs(fft_out))
# plt.show()
