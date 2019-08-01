# Black_Hole is derived from the Simulton: each updates by finding and removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10 
    
    def __init__(self,x,y):
        Simulton.__init__(self, x, y, self.radius*2, self.radius*2)
        self._color = 'black'
        
    def update(self, model, prey_type = lambda s : isinstance(s, Prey)):
        prey_consumed = model.find(lambda s: self.contains(s.get_location()) and prey_type(s))
        for p in prey_consumed: 
            model.remove(p)
        return prey_consumed
    
    def display(self, canvas):
        radius = self.get_dimension()[0]/2
        canvas.create_oval(self._x - radius, self._y - radius, self._x + radius, self._y + radius, fill = self._color )