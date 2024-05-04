import threading

import numpy as np
import sounddevice as sd

sample_rate = 22050  # Define sample_rate as a global variable


def generate_tone(frequency, duration, volume=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = volume * np.sin(frequency * t * np.pi).astype(np.float32)
    return tone  # Generate mono sound


def play_music(frequencies, player):
    duration = 0.2
    tones = [generate_tone(f, duration) for f in frequencies]

    def play_tones():
        for tone in tones:
            if player.stop:
                return
            sd.play(tone, samplerate=sample_rate, blocking=True)

    threading.Thread(target=play_tones).start()
