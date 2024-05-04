import pygame

from music import play_music


class Player:
    def __init__(self, location):
        self.location = location
        self.inventory = []
        self.health = 100
        self.stop = False
        self.picking_up = False
        self.play_music()

    def move(self, location):
        self.stop_music()
        pygame.time.wait(200)
        self.location = location
        self.play_music()

    def pick_up(self, item):
        self.inventory.append(item)
        self.location.items.remove(item)

    def play_music(self):
        self.stop = False
        play_music(self.location.song, self)

    def stop_music(self):
        self.stop = True
