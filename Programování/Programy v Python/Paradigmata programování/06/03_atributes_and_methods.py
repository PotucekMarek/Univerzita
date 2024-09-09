class Pair:
    """Spojí dvě hodnoty dohromady."""
    def __init__(self):
        self.first = None
        self.second = None

    def get_first(self):
        return self.first
    
    def set_first(self, value):
        self.first = value
        return self

    def get_second(self):
        return self.second

    def set_second(self, value):
        self.second = value
        return self

pair1 = Pair().set_first(1).set_second(2)
"""
>>> pair1.get_first()
1
>>> pair1.get_second()
2
"""

pair2 = Pair().set_first(3).set_second(4)
"""
>>> pair2.get_first()
3
>>> pair2.get_second()
4
"""

# Atribut můžeme přidat pouze jednomu objektu:
"""
>>> pair1.doc = "První pár"
>>> pair1.doc
'První pár'
>>> dir(pair1)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'doc', 'first', 'get_first', 'get_second', 'second', 'set_first', 'set_second']
"""

# Druhý objekt atribut doc nemá:
"""
>>> pair2.doc
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    pair2.doc
AttributeError: 'Pair' object has no attribute 'doc'
"""

# Můžeme získat metodu objektu:
"""
>>> pair1.get_first
<bound method Pair.get_first of <__main__.Pair object at 0x7f998910f520>>
>>> f = pair1.get_first
>>> f()
1
"""

# Tedy metody jsou atributy, které mají jako hodnotu funkce.
# Proto se v Pythonu musí názvy atribtů a metod lišit.
