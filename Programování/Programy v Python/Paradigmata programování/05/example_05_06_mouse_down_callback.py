# Převzato z materiálů Michala Krupky k předmětu Paradigmata programování 3.
# Přeloženo z Common Lispu do Pythonu.

import micro_graphic as mg

# Testování zpětného volání mouse_down 

w = mg.display_window()
mg.set_callback(w, "mouse_down", lambda w, button, x, y: print("Stisknutou tlačítko:", button, "Souřadnice:", [x, y]))



# Nakreslí kružnici na kliknutí
"""
mg.set_callback(w, "mouse_down", lambda w, button, x, y: mg.draw_circle(w, x, y, 30))
"""


# Kombinace zpětných volání display a mouse_down
position = [100, 50]

def display_function(w):
    mg.clear(w)
    mg.draw_circle(w, position[0], position[1], 30)

def mouse_down_function(w, button, x, y):
    position[0] = x
    position[1] = y
    mg.invalidate(w)

"""
mg.set_callback(w, "display", display_function)
mg.set_callback(w, "mouse_down", mouse_down_function)
"""
