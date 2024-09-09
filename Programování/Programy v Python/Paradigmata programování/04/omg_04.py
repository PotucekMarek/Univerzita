# Převzato z materiálů Michala Krupky k předmětu Paradigmata programování 3.
# Přeloženo z Common Lispu do Pythonu a trochu upraveno.
#
# Knihovna funguje pouze z prostředí IDLE.
# V jiných případech je potřeba na závěr programu
# oknu poslat zprávu mainloop bez argumentů.
#
# Například soubor test.py:
#
# from omg_04 import *
# w = Window()
# c = Circle().set_radius(30).move(100, 100)
# w.set_shape(c)
# w.redraw()
# w.mainloop()
#
# Spustíme z příkazové řádky: python3 test.py

import math
import micro_graphic as mg

def signum(number):
    if number < 0:
        return -1
    elif number > 0:
        return 1
    else:
        return 0

    
def is_number(value):
    return type(value) in [float, int]

class Shape:
    def __init__(self):
        self.color = "black"
        self.thickness = 1
        self.filled = False

    # Vlastnosti související s kreslením

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color
        return self

    def get_thickness(self):
        return self.thickness

    def set_thickness(self, thickness):
        self.thickness = thickness
        return self

    def get_filled(self):
        return self.filled

    def set_filled(self, filled):
        self.filled = filled
        return self

    # Kreslení

    def set_mg_params(self, mg_window):
        mg.set_param(mg_window, "foreground", self.get_color())
        mg.set_param(mg_window, "thickness", self.get_thickness())
        mg.set_param(mg_window, "filled", self.get_filled())
        return self

    def do_draw(self, mg_window):
        return self
    
    def draw(self, mg_window):
        self.set_mg_params(mg_window)
        self.do_draw(mg_window)
        return self

    # Geometrické transformace

    def move(self, dx, dy):
        return self

    def rotate(self, angle, center):
        return self

    def scale(self, coeff, center):
        return self
    
    
class Point(Shape):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        
    # Základní vlastnosti
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_x(self, x):
        if not is_number(x):
            raise TypeError("x coordinate of a point should be a number")
        self.x = x
        return self
    
    def set_y(self, y):
        if not is_number(y):
            raise TypeError("y coordinate of a point should be a number")       
        self.y = y
        return self

    def get_r(self):
        x = self.get_x()
        y = self.get_y()
        return math.sqrt((x ** 2) + (y ** 2))

    def get_phi(self):
        x = self.get_x()
        y = self.get_y()       
        if x > 0:
            return math.atan(y / x)
        elif x < 0:
            return math.pi + math.atan( y / x )
        else:
            return signum(y) * (math.pi / 2)

    def set_r_phi(self, r, phi):
        self.set_x(r * math.cos(phi))
        self.set_y(r * math.sin(phi))
        return self

    def set_r(self, r):
        return self.set_r_phi(r, self.get_phi())

    def set_phi(self, phi):
        return self.set_r_phi(self.get_r(), phi)



    # Kreslení

    def set_mg_params(self, mg_window):
        super().set_mg_params()
        mg.set_param(mg_window, "filled", True)
        return self

    def do_draw(self, mg_window):
        mg.draw_circle(mg_widnow, self.get_x(), self.get_y(), self.get_thickness())
        return self

    # Geometrické transformace

    def move(self, dx, dy):
        self.set_x(self.get_x() + dx)
        self.set_y(self.get_y() + dy)
        return self

    def rotate(self, angle, center):
        cx = center.get_x()
        cy = center.get_y()
        self.move(-cx, -cy)
        self.set_phi(self.get_phi() + angle)
        self.move(cx, cy)
        return self

    def scale(self, coeff, center):
        cx = center.get_x()
        cy = center.get_y()
        self.move(-cx, -cy)
        self.set_r(self.get_r() * coeff)
        self.move(cx, cy)
        return self
    

class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.center = Point()
        self.radius = 1

    # Geometrie
        
    def get_radius(self):
        return self.radius
    
    def set_radius(self, radius):
        if radius <= 0:
            raise ValueError("Circle radius should be a positive number")
        self.radius = radius
        return self
    
    def get_center(self):
        return self.center


    # Kreslení

    def do_draw(self, mg_window):
        mg.draw_circle(mg_window, self.get_center().get_x(), self.get_center().get_y(), self.get_radius())
        return self

    # Geometrické transformace

    def move(self, dx, dy):
        self.get_center().move(dx, dy)
        return self

    def rotate(self, angle, center):
        self.get_center().rotate(angle, center)
        return self

    def scale(self, coeff, center):
        self.get_center().scale(coeff, center)
        self.set_radius(self.get_radius() * coeff)
        return self

class CompoundShape(Shape):
    def __init__(self):
        super().__init__()
        self.items = []

    # Práce s atributem items

    def get_items(self):
        return self.items[:]

    def check_item(self, item):
        raise NotImplementedError("Method check_item of CompoundShape must be rewritten.")
            
    def set_items(self, items):
        for item in items:
            self.check_item(item)
        self.items = items[:]
        return self

    # Geometrické transformace
    
    def move(self, dx, dy):
        for item in self.get_items():
            item.move(dx, dy)
        return self

    def rotate(self, angle, center):
        for item in self.get_items():
            item.rotate(angle, center)
        return self

    def scale(self, coeff, center):
        for item in self.get_items():
            item.scale(coeff, center)
        return self
        
class Polygon(CompoundShape):
    def __init__(self):
        super().__init__()
        self.closed = True

    # Vlastnost vertices

    def get_vertices(self):
        return self.vertices[:]

    def check_item(self, item):
        if not isinstance(item, Point):
            raise ValueError("Items of polygon must be points.")
        return self

    # Vlastnosti související s kreslením


    def get_closed(self):
        return self.closed

    def set_closed(self, closed):
        self.closed = closed
        return self

    # Kreslení

    def get_polygon_coordinates(self):
        coordinates = []
        for item in self.get_items():
            coordinates += [item.get_x(), item.get_y()]
        return coordinates

    def set_mg_params(self, mg_window):
        super().set_mg_params(mg_window)
        mg.set_param(mg_window, "closed", self.get_closed())

    def do_draw(self, mg_window):
        mg.draw_polygon(mg_window, self.get_polygon_coordinates())


class Picture(CompoundShape):
    def check_item(self, item):
        if not isinstance(item, Shape):
            raise ValueError("Items of picture must be shapes.")

    # Kreslení

    def draw(self, mg_window):
        for item in self.get_items()[::-1]:
            item.draw(mg_window)
        return self

class Window:
    def __init__(self):
        self.mg_widnow = mg.display_window()
        self.shape = None
        self.background = "white"

    # Vlastnosti

    def get_shape(self):
        return self.shape

    def set_shape(self, shape):
        self.shape = shape
        return self

    def get_background(self):
        return self.background

    def set_background(self, background):
        self.background = background
        return self

    # Vykreslování

    def redraw(self):
        mgw = self.mg_widnow
        mg.set_param(mgw, "background", self.get_background())
        mg.clear(mgw)
        if self.get_shape():
            self.get_shape().draw(mgw)
        return self
    
    # Oživení okna mimo prostředí IDLE
    
    def mainloop(self):
        """Pokud se s knihovnou pracuje mimo prostředí IDLE,
            je potřeba tuto metodu zavolat na závěr programu."""
        mgw = self.mg_widnow
        mg.mainloop(mgw)

