''' Creating an item Class '''

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def take_item(self, player):
        pass

    def __str__(self):
        return self.description

class Money(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

class Health(Item):
    def __init__(self, name, description):
        super().__init__(name, description)