class Player:
    def __init__(self, location):
        self.health = 100  # Initialize player's health to 100
        self.inventory = []  # Initialize player's inventory as an empty list
        self.location = location  # Set player's initial location

    def render(self, font, screen):
        text = font.render(
            f"Health: {self.health}", True, (255, 255, 255)
        )  # Render player's health
        screen.blit(text, (50, 100))  # Display the health on the screen

    def pick_up(self, item):
        if item in self.location.items:  # If the item is in the current location
            self.location.items.remove(item)  # Remove the item from the location
            self.inventory.append(item)  # Add the item to the player's inventory
        else:
            print(
                f"There is no {item} here."
            )  # If the item is not in the location, print a message
