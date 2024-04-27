class Location:
    def __init__(self, description, items):
        self.description = description  # Description of the location
        self.items = items  # Items present in the location
        self.exits = {}  # Exits from the location

    def add_exit(self, direction, location, description):
        # Add an exit to another location
        self.exits[direction] = {"location": location, "description": description}

    def render(self, font, screen):
        # Render the location's description, exits, and items
        screen.blit(font.render(self.description, True, (255, 255, 255)), (50, 50))
        exits_text = "There lies a" + " and a".join(
            f" {exit['description']}" for direction, exit in self.exits.items()
        )
        screen.blit(font.render(f"{exits_text}", True, (255, 255, 255)), (50, 75))
        items_text = "You see the following items: " + ", ".join(self.items)
        screen.blit(font.render(items_text, True, (255, 255, 255)), (50, 100))
