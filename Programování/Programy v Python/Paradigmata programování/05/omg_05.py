# Převzato z materiálů Michala Krupky k předmětu Paradigmata programování 3.
# Přeloženo z Common Lispu do Pythonu a zjednodušeno.
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
        self.window = None
        self.ev_mouse_down = None

    # Vlastnosti související s kreslením

    def get_color(self):
        return self.color

    def do_set_color(self, color):
        self.color = color
        return self
        
    def set_color(self, color):
        self.do_set_color(color)
        self.change()
        return self

    def get_thickness(self):
        return self.thickness

    def do_set_thickness(self, thickness):
        self.thickness = thickness
        return self
    
    def set_thickness(self, thickness):
        self.do_set_thickness(thickness)
        self.change()
        return self

    def get_filled(self):
        return self.filled

    def do_set_filled(self, filled):
        self.filled = filled
        return self
    
    def set_filled(self, filled):
        self.do_set_filled(filled)
        self.change()
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

    def do_move(self, dx, dy):
        return self
    
    def move(self, dx, dy):
        self.do_move(dx, dy)
        self.change()
        return self

    def do_rotate(self, angle, center):
        return self
    
    def rotate(self, angle, center):
        self.do_rotate(angle, center)
        self.change()
        return self

    def do_scale(self, coeff, center):
        return self

    def scale(self, coeff, center):
        self.do_scale(coeff, center)
        self.change()
        return self

    # Změny

    def get_window(self):
        return self.window

    def set_window(self, window):
        self.window = window
        return self

    def change(self):
        window = self.get_window()
        if window:
            window.ev_change(self)
        return self

    # Práce s myší

    def get_ev_mouse_down(self):
        return self.ev_mouse_down

    def set_ev_mouse_down(self, function):
        self.ev_mouse_down = function
        return self

    def is_solid(self):
        return True

    def get_solid_shapes(self):
        if self.is_solid():
            return [self]
        else:
            return self.get_solid_subshapes()

    def get_solid_subshapes(self):
        raise NotImplementedError("Method has to be rewritten.")

    def contains_point(self, point):
        raise NotImplementedError("Method has to be rewritten.")

    def mouse_down(self, button, position):
        function = self.get_ev_mouse_down()
        if function:
            function(self, button, position)
        


def get_point_distance(point1, point2):
    x1 = point1.get_x()
    y1 = point1.get_y()
    x2 = point2.get_x()
    y2 = point2.get_y()
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
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
    
    def do_set_x(self, x):
        self.x = x
        return self

    def set_x(self, x):
        if not is_number(x):
            raise TypeError("x coordinate of a point should be a number")
        self.do_set_x(x)
        self.change()
        return self

    def do_set_y(self, y): 
        self.y = y
        return self
    
    def set_y(self, y):
        if not is_number(y):
            raise TypeError("y coordinate of a point should be a number")      
        self.do_set_y(y)
        self.change()
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
        super().set_mg_params(mg_window)
        mg.set_param(mg_window, "filled", True)
        return self

    def do_draw(self, mg_window):
        mg.draw_circle(mg_window, self.get_x(), self.get_y(), self.get_thickness())
        return self

    # Geometrické transformace

    def do_move(self, dx, dy):
        self.set_x(self.get_x() + dx)
        self.set_y(self.get_y() + dy)
        return self

    def do_rotate(self, angle, center):
        cx = center.get_x()
        cy = center.get_y()
        self.move(-cx, -cy)
        self.set_phi(self.get_phi() + angle)
        self.move(cx, cy)
        return self

    def do_scale(self, coeff, center):
        cx = center.get_x()
        cy = center.get_y()
        self.move(-cx, -cy)
        self.set_r(self.get_r() * coeff)
        self.move(cx, cy)
        return self

    # Práce s myší

    def contains_point(self, point):
        thickness = self.get_thickness()
        return get_point_distance(self, point) <= thickness

class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.center = Point()
        self.radius = 1

    # Geometrie
        
    def get_radius(self):
        return self.radius
    
    def do_set_radius(self, radius):
        self.radius = radius
        return self

    def set_radius(self, radius):
        if radius <= 0:
            raise ValueError("Circle radius should be a positive number")
        self.do_set_radius(radius)
        self.change()
        return self
    
    def get_center(self):
        return self.center

    # Vlastnost window

    def set_window(self, window):
        super().set_window(window)
        self.get_center().set_window(window)
        return self

    # Kreslení

    def do_draw(self, mg_window):
        mg.draw_circle(mg_window, self.get_center().get_x(), self.get_center().get_y(), self.get_radius())
        return self

    # Geometrické transformace

    def do_move(self, dx, dy):
        self.get_center().move(dx, dy)
        return self

    def do_rotate(self, angle, center):
        self.get_center().rotate(angle, center)
        return self

    def do_scale(self, coeff, center):
        self.get_center().scale(coeff, center)
        self.set_radius(self.get_radius() * coeff)
        return self

    # Práce s myší

    def contains_point(self, point):
        dist = get_point_distance(self.get_center(), point)
        radius = self.get_radius()
        if self.get_filled():
            return dist <= radius
        else:
            half_thickness = self.get_thickness() / 2
            return radius - half_thickness <= dist <= radius + half_thickness 

class CompoundShape(Shape):
    def __init__(self):
        super().__init__()
        self.items = []

    # Práce s atributem items

    def get_items(self):
        return self.items[:]

    def do_set_items(self, items):
        self.items = items[:]
        return self

    def check_item(self, item):
        raise NotImplementedError("Method check_item of CompoundShape must be rewritten.")

    def check_items(self, items):
        for item in items:
            self.check_item(item)

    def set_items_window(self, window):
        for item in self.get_items():
            item.set_window(window)    

    def set_items(self, items):
        self.check_items(items)
        self.set_items_window(None)
        self.do_set_items(items)
        self.set_items_window(self.get_window())
        self.change()
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

    # Změny

    def set_window(self, window):
        super().set_window(window)
        self.set_items_window(window)
        return self
        
class Polygon(CompoundShape):
    def __init__(self):
        super().__init__()
        self.closed = True

    # Vlastnost items


    def check_item(self, item):
        if not isinstance(item, Point):
            raise ValueError("Items of polygon must be points.")
        return self

    # Vlastnosti související s kreslením


    def get_closed(self):
        return self.closed

    def do_set_closed(self, closed):
        self.closed = closed
        return self
    
    def set_closed(self, closed):
        self.do_set_closed(closed)
        self.change()
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

    # Práce s myší

    def contains_point(self, point):
        return mg.is_point_in_polygon(point.get_x(),
                                      point.get_y(),
                                      self.get_closed(),
                                      self.get_filled(),
                                      self.get_thickness(),
                                      self.get_polygon_coordinates())
                                      


class Picture(CompoundShape):
    def check_item(self, item):
        if not isinstance(item, Shape):
            raise ValueError("Items of picture must be shapes.")

    # Kreslení

    def draw(self, mg_window):
        for item in self.get_items()[::-1]:
            item.draw(mg_window)
        return self

    # Práce s myší
    
    def is_solid(self):
        return False

    def get_solid_subshapes(self):
        result = []
        for item in self.get_items():
            result += item.get_solid_shapes()
        return result

    def contains_point(self, point):
        for item in self.get_items():
            if item.contains_point(point):
                return True
        return False

class Window:
    def __init__(self):
        self.mg_window = mg.display_window()
        self.shape = None
        self.background = "white"
        self.install_callbacks()

    # Zpětná volání

    def install_callbacks(self):
        self.install_display_callback()
        self.install_mouse_down_callback()

    def install_display_callback(self):
        mg.set_callback(self.mg_window, "display",
                        lambda mgw: self.redraw())

    def install_mouse_down_callback(self):
        mg.set_callback(self.mg_window, "mouse_down",
                        lambda mgw, button, x, y: self.window_mouse_down(button, Point().move(x, y)))

    # Vlastnosti

    def get_shape(self):
        return self.shape

    def set_shape(self, shape):
        if self.get_shape():
            self.get_shape().set_window(None)
        self.shape = shape
        if shape:
            shape.set_window(self)
        self.invalidate()
        return self

    def get_background(self):
        return self.background

    def set_background(self, background):
        self.background = background
        self.invalidate()
        return self

    # Vykreslování

    def redraw(self):
        mgw = self.mg_window
        mg.set_param(mgw, "background", self.get_background())
        mg.clear(mgw)
        if self.get_shape():
            self.get_shape().draw(mgw)
        return self

    # Změny

    def ev_change(self, shape):
        self.invalidate()

    def invalidate(self):
        mg.invalidate(self.mg_window)
        return self

    # Práce s myší

    def find_clicked_shape(self, position):
        shape = self.get_shape() 
        if shape:
            solid_shapes = shape.get_solid_shapes()
            for solid_shape in solid_shapes:
                if solid_shape.contains_point(position):
                    return solid_shape

    def mouse_down_inside_shape(self, shape, button, position):
        shape.mouse_down(button, position)
        return self

    def mouse_down_no_shape(self, button, position):
        return self

    def window_mouse_down(self, button, position):
        shape = self.find_clicked_shape(position)
        if shape:
            self.mouse_down_inside_shape(shape, button, position)
        else:
            self.mouse_down_no_shape(button, position)
        return self
    
    # Oživení okna mimo prostředí IDLE
    
    def mainloop(self):
        """Pokud se s knihovnou pracuje mimo prostředí IDLE,
            je potřeba tuto metodu zavolat na závěr programu."""
        mgw = self.mg_window
        mg.mainloop(mgw)

