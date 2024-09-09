# Převzato z materiálů Michala Krupky k předmětu Paradigmata programování 3.
# Přeloženo z Common Lispu do Pythonu.
from random import randrange
from omg_05 import *

def random_color():
    color = mg.make_color_rgb(randrange(256), randrange(256), randrange(256))
    return color

class ClickCircle(Circle):
    def __init__(self):
        super().__init__()
        self.set_ev_mouse_down(lambda self, button, position: self.set_random_color())

    def set_random_color(self):
        self.set_color(random_color())
        

def make_test_click_circle():
    circle = ClickCircle()
    return circle.set_radius(45).set_filled(True)

# Jedno klikací kolečko
"""
w = Window()
c = make_test_click_circle().move(148, 100)
w.set_shape(c)
"""

# Čtyři klikací kolečka
"""
w = Window()
circles = Picture()
circles.set_items([
    make_test_click_circle().move(103, 55),
    make_test_click_circle().move(193, 55),
    make_test_click_circle().move(103, 145),
    make_test_click_circle().move(193, 145)])
w.set_shape(circles)
"""
