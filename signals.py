import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

import sounddevice as sd
import soundfile as sf

def play_sound(sound, fs):
    sd.play(sound, fs)
    sd.wait()

def read_sound(file):
    sound, fs = sf.read(file, dtype='float32')
    return sound, fs

def test_signal(N=2000, fs=2000):
    x = np.linspace(0, N / fs, N, endpoint=False)
    y = 0.1 * np.sin(440 * 2 * np.pi * x) + 0.2 * np.sin(5 / 4 * 440 * 2 * np.pi * x) + 0.3 * np.sin(3 / 2 * 440 * 2 * np.pi * x)

    return y, fs
    
def read_vowel(vowel):
    signal, fs = read_sound(vowel + ".wav")
    return signal, fs

def read_bh_collsision():
    signal, fs = read_sound("BlackHolesCollision.wav")
    signal = signal[:, 0]
    return signal, fs

def plot_signal(signal, fs):
    x = np.linspace(0, len(signal) / fs, len(signal), endpoint=False)

    plt.plot(x, signal)
    plt.xlabel("$t$ [s]")
    plt.ylabel("$y$")
    plt.show()

signal, fs = test_signal()
play_sound(signal, fs)
plot_signal(signal, fs)

signal, fs = read_vowel('a')
play_sound(signal, fs)
plot_signal(signal, fs)

signal, fs = read_bh_collsision()
play_sound(signal, fs)
plot_signal(signal, fs)