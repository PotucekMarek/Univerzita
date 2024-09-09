# Převzato z materiálů Michala Krupky k předmětu Paradigmata programování 3.
# Přeloženo z Common Lispu do Pythonu.

from omg_05 import *

w = Window()

def make_test_circle():
    return Circle().set_color("darkslategrey").set_thickness(5).set_radius(55).move(148, 100)
    

"""
w.set_background("azure")
w.set_shape(make_test_circle())
"""
