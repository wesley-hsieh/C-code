# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole
from prey import Prey

class Pulsator(Black_Hole): 
    time = 30
    
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self.counter = 0
    
    def update(self, model, prey_type = lambda s: isinstance(s, Prey)):
        preyed = Black_Hole.update(self, model, prey_type)
        if len(preyed) > 0:
            self.counter = 0
            self.change_dimension(len(preyed), len(preyed))
        else:
            self.counter += 1
            if self.counter == Pulsator.time:
                self.counter = 0
                self.change_dimension(-1, -1)
                if self.get_dimension() == (0, 0):
                    model.remove(self)
