import numpy as np
import pygame


def generate_wave(frequency, duration, sample_rate=44100):
    t = np.linspace(
        0, duration, int(sample_rate * duration), False
    )  # Generate time array
    return (np.sin(frequency * t * 2 * np.pi) * 32767).astype(
        np.int16
    )  # Generate sine wave


def play_music():
    pygame.mixer.init()  # Initialize the mixer module
    frequencies = [
        220.00,
        261.63,
        293.66,
        329.63,
        392.00,
        493.88,
        369.99,
        415.30,
    ]  # Define frequencies for the notes
    bass_frequencies = [
        f / 2 for f in frequencies
    ]  # Define frequencies for the bass notes
    notes = [generate_wave(f, 0.5) for f in frequencies]  # Generate waves for the notes
    bass_notes = [
        generate_wave(f, 0.5) for f in bass_frequencies
    ]  # Generate waves for the bass notes
    music = np.vstack(
        [np.hstack(notes * 24), np.hstack(bass_notes * 24)]
    ).T  # Stack the notes and bass notes to create the music
    pygame.mixer.Sound(buffer=music.astype(np.int16).tobytes()).play()  # Play the music
