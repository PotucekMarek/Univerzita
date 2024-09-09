import numbers

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

    # Součet vektorů.

    def __add__(self, vec2):
        if not isinstance(vec2, Vect):
            return NotImplemented # Systém zkusí otočit pořadí operandů v +
        x = self.get_x() + vec2.get_x()
        y = self.get_y() + vec2.get_y()
        return Vect().set_x(x).set_y(y)

    # Násobení vektoru a čísla.
    
    def __mul__(self, num):
        if not isinstance(num, numbers.Number):
            return NotImplemented # Systém zkusí otočit pořadí operandů v *
        x = num * self.get_x()
        y = num * self.get_y()
        return Vect().set_x(x).set_y(y)

    # Násobení čísla a vektoru.
    
    def __rmul__(self, arg):
        return self * arg


v1 = Vect().set_x(1).set_y(2)
v2 = Vect().set_x(3).set_y(4)

# Sčítání vektorů.

"""
v3 = v1 + v2
>>> v3.get_x()
4
>>> v3.get_y()
6
"""

# Násobení vektoru číslem.
"""
>>> v4 = v1 * 3
>>> v4.get_x()
3
>>> v4.get_y()
6
"""

# Využití __rmul__:
"""
>>> v5 = 3 * v1
>>> v5.get_x()
3
>>> v5.get_y()
6
"""
