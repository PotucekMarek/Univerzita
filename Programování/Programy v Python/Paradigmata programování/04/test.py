from omg_04 import *

w = Window()
c = Circle().set_radius(30).move(100, 100)
w.set_shape(c)
w.redraw()
w.mainloop()
