# Převzato z materiálů Michala Krupky k předmětu Paradigmata programování 3.
# Přeloženo z Common Lispu do Pythonu.

import micro_graphic as mg

mgw = mg.display_window()
mg.set_callback(mgw, "display", lambda mgw: print("Překresli mě"))


# Invalidate okna:
"""
mg.invalidate(mgw)
"""

# Překreslí se pouze jednou:
"""
for i in range(100):
    mg.invalidate(mgw)
"""

radius = 50

def mg_draw(mgw):
    mg.set_param(mgw, "background", "white")
    mg.clear(mgw)
    mg.set_param(mgw, "foreground", "black")
    mg.draw_circle(mgw, 143, 105, radius)

# Změníme zpětné volání:

mg.set_callback(mgw, "display", mg_draw)
radius = 30
mg.invalidate(mgw)

