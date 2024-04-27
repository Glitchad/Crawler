import pygame


class Location:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.exits = {}

    def add_exit(self, direction, location, description):
        self.exits[direction] = {"location": location, "description": description}

    def render(self, font, screen, player):
        screen.fill((0, 0, 0))  # Clear the screen
        self.render_description(font, screen)
        self.render_inventory_and_health(font, screen, player)
        self.render_items(font, screen)
        self.render_exits(font, screen)
        pygame.display.flip()
        pygame.time.wait(500)  # Wait for 500 milliseconds

    def render_description(self, font, screen):
        words = self.description.split()
        for i, word in enumerate(words):
            word_surface = font.render(word, True, (255, 255, 255))
            screen.blit(word_surface, (50, 50 + i * 20))

    def render_inventory_and_health(self, font, screen, player):
        self.render_text(font, screen, f"Inventory: {player.inventory}", 50, 200)
        self.render_text(font, screen, f"Health: {player.health}", 50, 220)

    def render_items(self, font, screen):
        self.render_text(font, screen, f"Items: {self.items}", 50, 240)

    def render_exits(self, font, screen):
        self.render_text(font, screen, f"Exits: {list(self.exits.keys())}", 50, 260)

    def render_text(self, font, screen, text, x, y):
        text_surface = font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, (x, y))
