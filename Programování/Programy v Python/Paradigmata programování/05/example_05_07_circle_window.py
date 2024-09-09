# Převzato z materiálů Michala Krupky k předmětu Paradigmata programování 3.
# Přeloženo z Common Lispu do Pythonu.

from omg_05 import *

def make_test_circle():
    return Circle().set_color("darkslategrey").set_thickness(3).set_radius(55).move(148, 100)

class CircleWindow(Window):
    def __init__(self):
        super().__init__()
        self.set_shape(make_test_circle())
        
    def window_mouse_down(self, button, position):
        if button == "left":
            circle = self.get_shape()
            center = circle.get_center()
            dx = position.get_x() - center.get_x()
            dy = position.get_y() - center.get_y()
            circle.move(dx, dy)


w = CircleWindow()
