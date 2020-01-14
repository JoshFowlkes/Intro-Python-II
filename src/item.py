''' Creating an item Class '''

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def take_item(self, player):
        pass

    def __str__(self):
        return self.description