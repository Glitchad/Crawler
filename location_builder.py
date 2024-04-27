from location import Location


class LocationBuilder:
    def __init__(self):
        self.location = Location("", [])

    def with_description(self, description):
        self.location.description = description
        return self

    def with_items(self, items):
        self.location.items = items
        return self

    def build(self):
        return self.location
