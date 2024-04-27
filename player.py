class Player:
    def __init__(self, location):
        self.health = 100
        self.inventory = []
        self.location = location

    def render(self, font, screen):
        text = font.render(f"Health: {self.health}", True, (255, 255, 255))
        screen.blit(text, (50, 100))

    def pick_up(self, item):
        if item in self.location.items:
            self.location.items.remove(item)
            self.inventory.append(item)
        else:
            print(f"There is no {item} here.")
