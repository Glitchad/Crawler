from location import Location


class World:
    def __init__(self):
        self.locations = {
            "forest": Location("forest", "You are in a forest.", ["a rusty sword"]),
            "cave": Location("cave", "You are in a cave.", ["a battered shield"]),
            "cottage": Location(
                "cottage", "You are in a cottage.", ["a gleaming potion"]
            ),
        }

        self.locations["forest"].add_exit(
            "west", self.locations["cottage"], "small cottage to the West"
        )
        self.locations["forest"].add_exit(
            "north", self.locations["cave"], "dark cave to the North."
        )
        self.locations["cave"].add_exit(
            "south", self.locations["forest"], "lush forest to the South."
        )
        self.locations["cottage"].add_exit(
            "east", self.locations["forest"], "lush forest to the East."
        )
