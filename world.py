from location_builder import LocationBuilder


class World:
    def __init__(self):
        builder = LocationBuilder()

        forest = (
            builder.with_description("You are in a forest.")
            .with_items(["a rusty sword"])
            .build()
        )
        cave = (
            builder.with_description("You are in a cave.")
            .with_items(["a battered shield"])
            .build()
        )
        cottage = (
            builder.with_description("You are in a cottage.")
            .with_items(["a gleaming potion"])
            .build()
        )

        forest.add_exit("west", cottage, "small cottage to the West")
        forest.add_exit("north", cave, "dark cave to the North.")
        cave.add_exit("south", forest, "lush forest to the South.")
        cottage.add_exit("east", forest, "lush forest to the East.")

        self.locations = {forest.name: forest, cave.name: cave, cottage.name: cottage}
