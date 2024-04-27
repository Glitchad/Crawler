import numpy as np
import pygame


def generate_tone(frequency, duration, volume=0.5, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    return (volume * np.sin(frequency * t * np.pi)).astype(np.float32)


def play_music():
    pygame.mixer.init()
    pygame.mixer.set_num_channels(8)

    frequencies = [
        261.63,
        293.66,
        329.63,
        349.23,
        392.00,
        440.00,
        493.88,
        523.25,
    ]  # C major scale
    duration = 0.5  # Each note lasts for half a second

    for i, f in enumerate(frequencies):
        tone = generate_tone(f, duration)
        sound = pygame.mixer.Sound(tone.tobytes())
        pygame.mixer.Channel(i).play(sound)
        pygame.time.wait(
            int(duration * 1000)
        )  # Wait for the duration of the note before playing the next one
