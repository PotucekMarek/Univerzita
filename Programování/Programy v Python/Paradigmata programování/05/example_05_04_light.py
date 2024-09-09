# Převzato z materiálů Michala Krupky k předmětu Paradigmata programování 3.
# Přeloženo z Common Lispu do Pythonu.

from omg_05 import *

class Light(Circle):
    def __init__(self):
        super().__init__()
        self.on = True
        self.on_color = "red"
        self.off_color = "grey"
        
        self.set_filled(True)
        self.ensure_color()

    def get_on(self):
        return self.on

    def set_on(self, on):
        self.on = on
        self.ensure_color()
        return self

    def get_on_color(self):
        return self.on_color

    def set_on_color(self, on_color):
        self.on_color = on_color
        self.ensure_color()
        return self

    def get_off_color(self):
        return self.off_color

    def set_off_color(self, off_color):
        self.off_color = off_color
        self.ensure_color()
        return self

    def ensure_color(self):
        if self.get_on():
            color = self.get_on_color()
        else:
            color = self.get_off_color()
        self.set_color(color)
        return self

    def toggle(self):
        self.set_on(not self.get_on())
        return self

    def turn_on(self):
        self.set_on(True)

    def turn_off(self):
        self.set_on(False)
    
w = Window()
light = Light().set_radius(50).move(100, 100)
w.set_shape(light)

"""
light.toggle()
light.set_on_color("green")
light.turn_on()

"""
