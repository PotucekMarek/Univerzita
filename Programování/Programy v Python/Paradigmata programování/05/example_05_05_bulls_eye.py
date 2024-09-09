# Převzato z materiálů Michala Krupky k předmětu Paradigmata programování 3.
# Přeloženo z Common Lispu do Pythonu.

from omg_05 import *

class BullsEye(Picture):
    def __init__(self):
        super().__init__()
        self.set_items(make_be_items(0, 0, 1, 1))

    def get_circle_count(self):
        return len(self.get_items())

    def set_circle_count(self, count):
        if count <= 0:
            raise ValueError("Circle count must be positive.")
        x = self.get_center().get_x()
        y = self.get_center().get_y()
        radius = self.get_radius()
        self.set_items(make_be_items(x, y, radius, count))
        return self

    def get_radius(self):
        return self.get_items()[-1].get_radius()

    def get_center(self):
        return self.get_items()[0].get_center()

    def set_radius(self, radius):
        self.scale(radius / self.get_radius(), self.get_center())
        return self

def make_be_item (x, y, radius, black):
    if black:
        color = "black"
    else:
        color = "white"
    return Circle().set_radius(radius).set_color(color).set_filled(True).move(x, y)

def make_be_items(x, y, radius, count):
    result = []
    for i in range(1, count + 1):
        result += [make_be_item(x, y, radius * (i / count), i % 2 == 1)]
    return result



w = Window()
be = BullsEye().move(145, 97).set_circle_count(7).set_radius(80)
w.set_shape(be)
w.set_shape(be)
be.set_radius(60)
be.set_circle_count(5)

