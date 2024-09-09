# Všechny hodnoty v Pythonu jsou objekty ve smyslu objektového programování.
# Tedy i čísla jsou objekty.

# Například součet čísel:
"""
>>> 1 + 2
3
"""

# Vede k zaslání systémové zprávy __add__:
"""
>>> (1).__add__(2)
3
"""
# Jednička musí být v závorkách, protože 1.__add__ by interpret
# chápal jako špatně zadané desetinné číslo.

# Zprávy, kterým objekt rozumí, lze získat vestavěnou funkcí dir:
"""
>>> dir(1)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

"""

# To, že součet seznamů vede k jejich spojení,
# je docíleno polymorfismem:
"""
>>> [1] + [2]
[1, 2]
>>> [1].__add__([2])
[1, 2]
"""

# Zjištění třídy, jejíž je objekt přímou instancí.
"""
>>> type(1)
<class 'int'>
>>> type(0.1)
<class 'float'>
>>> type([1, 2])
<class 'list'>
"""

# Ověření, zda je objekt instancí systémové třídy.
"""
>>> isinstance(1, int)
True
>>> isinstance(1.0, int)
False
"""

# Všechny čísla jsou instancí třídy numbers.Number:
"""
>>> import numbers
>>> isinstance(1, numbers.Number)
True
>>> isinstance(1.0, numbers.Number)
True
"""
