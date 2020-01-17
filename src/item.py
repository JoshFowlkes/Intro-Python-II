''' Creating an item Class '''

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def take_item(self, player):
        pass
    def __repr__(self):
        return self.description

class Gold(Item):
    'gold class inheriting from the parent item class '
    def __init__(self, name, description, value):
        self.value = value
        self.picked_up = False
        super().__init__(name, description)
    
    def take_item(self, player):
        super().take_item(player)

        if not self.picked_up:
            player.score += score.value
            print(f' {self.value} points!!')
            self.picked_up = True

