import threading

import numpy as np
import pygame


def generate_tone(frequency, duration, volume=0.5, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    return (volume * np.sin(frequency * t * np.pi)).astype(np.float32)


def play_music(frequencies):
    pygame.mixer.init()
    duration = 0.2  # Each note lasts for half a second

    def play_tones():
        for f in frequencies:
            tone = generate_tone(f, duration)
            sound = pygame.mixer.Sound(tone.tobytes())
            sound.play()
            pygame.time.wait(int(duration * 1000))

    threading.Thread(target=play_tones).start()
