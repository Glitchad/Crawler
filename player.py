import pygame

from music import play_music


class Player:
    def __init__(self, location):
        self.location = location
        self.inventory = []
        self.health = 100
        self.picking_up = False
        play_music(self.location.song)

    def move(self, location):
        pygame.mixer.stop()
        self.location = location
        play_music(self.location.song)

    def pick_up(self, item):
        self.inventory.append(item)
        self.location.items.remove(item)
