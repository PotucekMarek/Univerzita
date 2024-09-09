from random import randrange
from omg_05 import *
from example_05_08_click_circle import ClickCircle

def make_point(x, y):
    return Point().move(x, y)


def make_polygon_items(x_arr, y_arr, filled, closed, color):
    points = []
    for i in range(len(x_arr)):
        points += [make_point(x_arr[i], y_arr[i])] 
    return points

def make_arrow(color):
    return make_polygon_items([0, 0, 30, 30, 0, 0, -30],
                        [-30, -15, -15, 15, 15, 30, 0],
                        True,
                        True,
                        color)

class Arrow(Polygon):
    def __init__(self):
        super().__init__()
        self.set_items(make_arrow())
        self.set_filled(True)

    def start(self):
        return self.get_items()[3]
    
    def end(self):
        return self.get_items()[7]

    def get_direction_x(self):
        return self.end().get_x() - self.start().get_x
    
    def get_direction_y(self):
        return self.end().get_y() - self.start().get_y()



def cwas_items(count):
    items = [Circle().set_radius(60).set_filled(True)]
    for i in range(count):
        angle = i * (2 * math.pi / count)
        items += [Arrow().move(20).rotate(angle, Point())]

    return items


class CircleWithArrow(Picture):
    def __init__(self, count):
        super().__init__()
        self.set_items(cwas_items(count))
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
        

w = CWAWindow()
c = CircleWithArrow(3).move(200,200)
input()
