# Převzato z materiálů Michala Krupky k předmětu Paradigmata programování 3.
# Přeloženo z Common Lispu do Pythonu a upraveno.

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


def make_arrow(color):
    return make_polygon([0, 0, 30, 30, 0, 0, -30],
                        [-30, -15, -15, 15, 15, 30, 0],
                        True,
                        True,
                        color)


def make_cwa_items():
    click_circle = ClickCircle().set_radius(40).set_filled(True).move(148, 60)
    arrow = make_arrow("blue").rotate(math.pi / 2, Point()).move(148, 150)
    return [click_circle, arrow]



class CircleWithArrow(Picture):
    def __init__(self):
        super().__init__()
        self.set_items(make_cwa_items())
        self.get_cwa_arrow().set_ev_mouse_down(lambda sender, button, position: self.arrow_click())
        
    def arrow_click(self):
        self.get_cwa_circle().move(0, -10)
        
    def get_cwa_circle(self):
        return self.get_items()[0]

    def get_cwa_arrow(self):
        return self.get_items()[1]    


class CWAWindow(Window):
    def __init__(self):
        super().__init__()
        self.set_shape(CircleWithArrow())
        

CWAWindow()
