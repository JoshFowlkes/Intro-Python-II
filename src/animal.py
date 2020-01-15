class MANimal:
    def __init__(self, name, legs, planet='Earth'):
        self.name = name
        self.legs = legs
        self.planet = planet
    #@abstractmethod
    def speak(self):
        pass
    #@abstractmethod
    def species(self):
        pass

''' inheriting from the class above ''' 
class Dog(MANimal):
    def __init__(self, name, legs=4, planet='Earth'):
        super().__init__(name, legs, planet)
    def speak(self):
        print('Bark!')
    def species(self):
        print('Dog')

class Bird(MANimal):
    def __init__(self, name, legs=2):
        super().__init__(name, legs)
    def speak(self):
        print('Tweet!')
    def species(self):
        print('Bird')

