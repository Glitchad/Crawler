import pygame

from renderer import Renderer


class Location:
    def __init__(self, name, description, items):
        self.name, self.description, self.items = name, description, items
        self.exits = {}

    def add_exit(self, direction, location, description):
        self.exits[direction] = {"location": location, "description": description}

    def render(self, font, screen, player):
        screen.fill((0, 0, 0))
        Renderer.render_status(font, screen, player)
        Renderer.render_items(font, screen, self.items)
        Renderer.render_description(font, screen, self.description)
        Renderer.render_exits(font, screen, self.exits)
        pygame.display.flip()
