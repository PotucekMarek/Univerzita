class Colored:
    def __init__(self):
        super().__init__() # Nutné.
        self.color = "black"

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color
        return self

class Vect:
    def __init__(self):
        self.x = 0
        self.y = 0

    def get_x(self):
        return self.x

    def set_x(self, value):
        self.x = value
        return self

    def get_y(self):
        return self.y

    def set_y(self, value):
        self.y = value
        return self

class ColoredVect(Colored, Vect):
    pass

# Třída ColoredVect dědí jak z třídy Colored tak Vect.
"""
>>> v = ColoredVect()
>>> v.get_color()
'black'
>>> v.get_x()
0
>>> v.get_y()
0
>>> v.set_color("blue")
<__main__.ColoredVect object at 0x7fdc5840b0d0>
>>> v.get_color()
'blue'
"""
