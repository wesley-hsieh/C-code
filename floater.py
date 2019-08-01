# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    def __init__(self, x, y):
        self.radius = 5
        Prey.__init__(self, x, y, self.radius*2, self.radius*2,0,5)
        self.randomize_angle()
        
    def update(self, model):
        Prey.move(self)
        num = random()
        if num >= 0.7 : 
            self.set_angle(self.get_angle() + (0.5 - random()))
            self.set_speed(self.get_speed() + (0.5 - random()))
            if self.get_speed() < 3.0:  
                self.set_speed(3.0)
            if self.get_speed() > 7.0: 
                self.set_speed(7.0)
        
        
    def display(self, canvas):
        canvas.create_oval(self._x - self.radius, self._y - self.radius, self._x + self.radius, self._y + self.radius)
            
