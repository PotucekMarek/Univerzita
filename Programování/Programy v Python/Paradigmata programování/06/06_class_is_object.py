class MyList:
    pass

# Třídy jsou objekty:
"""
>>> T = MyList
>>> l1 = T()
>>> l1
<__main__.MyList object at 0x7ff88a93bc70>
"""

# Třídy jsou instance třídy type:
"""
>>> type(MyList)
<class 'type'>
>>> isinstance(MyList, type)
True
"""

# Třída type je instancí sama sebe:
"""
>>> isinstance(type, type)
True
>>> type(type) == type
True
"""
