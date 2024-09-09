# Ukázka obrázku, na který lze klikat. (Je pevný.)

from random import randrange
from omg_05 import *
from example_05_08_click_circle import ClickCircle


def make_point(x, y):
    return Point().move(x, y)


def make_polygon(x_arr, y_arr, filled, closed, color):
    points = []
    for i in range(len(x_arr)):
        points += [make_point(x_arr[i], y_arr[i])] 
    return Polygon().set_items(points).set_filled(filled).set_closed(closed).set_color(color)


class CircleArrow(Picture):
    def __init__(self):
        super().__init__()
        circle = Circle().set_radius(50).set_filled(True)
        triangle = make_polygon([-50, 0, 50], [50, 100, 50], True, True, "red")
        self.set_items([circle, triangle])
        self.set_ev_mouse_down(lambda sender, button, position: self.rotate_step())
        
    def is_solid(self):
        return True

    def get_circle(self):
        return self.get_items()[0]

    def get_triangle(self):
        return self.get_items()[1]

    def rotate_step(self):
        circle = self.get_circle()
        center = circle.get_center()
        self.rotate(math.pi / 8, center)
    
w = Window()
ca = CircleArrow()
ca.move(147, 105)
w.set_shape(ca)
