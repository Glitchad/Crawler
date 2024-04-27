from location import Location


class World:
    def __init__(self):
        self.locations = {
            "cave": Location(
                "Cave",
                "A dark and damp cave.",
                ["torch", "key"],
                [
                    261.63,
                    440.00,
                    329.63,
                    783.99,
                    392.00,
                    659.25,
                    493.88,
                    587.33,
                    349.23,
                    698.46,
                    523.25,
                    1046.50,
                ],
            ),
            "forest": Location(
                "Forest",
                "A lush and green forest.",
                ["apple", "map"],
                [
                    349.23,
                    880.00,
                    440.00,
                    783.99,
                    523.25,
                    659.25,
                    493.88,
                    987.77,
                    392.00,
                    698.46,
                    587.33,
                    1046.50,
                ],
            ),
            "cottage": Location(
                "Cottage",
                "A cozy little cottage.",
                ["book", "pen"],
                [
                    392.00,
                    987.77,
                    493.88,
                    880.00,
                    587.33,
                    659.25,
                    523.25,
                    783.99,
                    440.00,
                    698.46,
                    349.23,
                    1174.66,
                ],
            ),
            # Add more locations...
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
