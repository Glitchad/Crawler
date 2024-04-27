from location import Location


class World:
    def __init__(self):
        # Initialize the world with three locations: forest, cave, and cottage
        forest = Location("You are in a forest.", ["a rusty sword"])
        cave = Location("You are in a cave.", ["a battered shield"])
        cottage = Location("You are in a cottage.", ["a gleaming potion"])

        # Add exits to other locations from each location
        forest.add_exit("west", cottage, "small cottage to the West")
        forest.add_exit("north", cave, "dark cave to the North.")
        cave.add_exit("south", forest, "lush forest to the South.")
        cottage.add_exit("east", forest, "lush forest to the East.")

        # Store the locations in a dictionary
        self.locations = {"forest": forest, "cave": cave, "cottage": cottage}
