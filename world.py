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

        self.add_exits()

    def add_exits(self):
        exits = {
            "forest": {"west": "cottage", "north": "cave"},
            "cave": {"south": "forest"},
            "cottage": {"east": "forest"},
        }

        descriptions = {
            "forest": {
                "west": "small cottage to the West",
                "north": "dark cave to the North.",
            },
            "cave": {"south": "lush forest to the South."},
            "cottage": {"east": "lush forest to the East."},
        }

        for location, exits in exits.items():
            for direction, exit in exits.items():
                self.locations[location].add_exit(
                    direction, self.locations[exit], descriptions[location][direction]
                )
