class Player:
    def __init__(self, location):
        self.location = location
        self.inventory = []
        self.health = 100
        self.picking_up = False

    def move(self, new_location):
        self.location = new_location

    def pick_up(self, item):
        self.inventory.append(item)
        self.location.items.remove(item)
