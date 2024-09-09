# Převzato z materiálů Michala Krupky k předmětu Paradigmata programování 3.
# Přeloženo z Common Lispu do Pythonu a trochu upraveno.

import tkinter

class MGWindow:
    def __init__(self):
        top = tkinter.Tk()
        top.title("micro_graphics window")
        canvas = tkinter.Canvas(top, width=297, height=210)
        canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
        canvas.bind('<ButtonPress>', lambda event: self.canvas_click(event.num, event.x, event.y))
        self.top = top
        self.canvas = canvas
        self.params = {"foreground": "black", "background": "white", "thickness": 1, "filled": False, "closed": False}
        self.valid = False
        self.callbacks = {}
        self.schedule_check_valid()

    def get_top(self):
        return self.top

    def get_canvas(self):
        return self.canvas

    def get_params(self):
        return self.params

    def get_valid(self):
        return self.valid

    def set_valid(self, valid):
        self.valid = valid
        return self

    def get_callbacks(self):
        return self.callbacks

    def schedule_check_valid(self):
        top = self.get_top()
        top.after(10, lambda: self.check_valid())

    def check_valid(self):
        if not self.get_valid():
            call_back(self, "display", [])
            self.set_valid(True)
        self.schedule_check_valid()

    def canvas_click(self, button_num, x, y):
        if button_num == 1:
            button = "left"
        elif button_num == 2:
            button = "right"
        else:
            button = None
        if button:
            call_back(self, "mouse_down", [button, x, y])


def invalidate(mg_window):
    mg_window.set_valid(False)


def call_back(mg_window, callback_name, args):
    fun = get_callback(mg_window, callback_name)
    if fun:
        fun(mg_window, *args)


def get_callback(mg_window, callback_name):
    callbacks = mg_window.get_callbacks()
    if callback_name in callbacks.keys():
        return callbacks[callback_name]


def set_callback(mg_window, callback_name, function):
    mg_window.get_callbacks()[callback_name] = function
    if callback_name == "display":
        invalidate(mg_window)
        
        
def display_window():
    return MGWindow()


def get_param(mg_window, param):
    params = mg_window.get_params()
    return params[param]


def set_param(mg_window, param, value):
    params =  mg_window.get_params()
    params[param] = value
    return mg_window


def draw_circle(mg_window, x, y, r):
    canvas = mg_window.get_canvas()
    filled = get_param(mg_window, "filled")
    if filled:
        background = get_param(mg_window, "foreground")
        canvas.create_oval(x - r, y - r, x + r, y + r, fill=background, outline="")
    else:
        foreground = get_param(mg_window, "foreground")
        thickness = get_param(mg_window, "thickness")
        canvas.create_oval(x - r, y - r, x + r, y + r, fill="", outline=foreground, width=thickness)


def draw_polygon(mg_window, points):
    canvas = mg_window.get_canvas()
    filled = get_param(mg_window, "filled")
    if filled:
        background = get_param(mg_window, "foreground")
        canvas.create_polygon(points, fill=background, outline="")
    else:
        foreground = get_param(mg_window, "foreground")
        thickness = get_param(mg_window, "thickness")
        closed = get_param(mg_window, "closed")
        if closed:
            canvas.create_polygon(points, outline=foreground, width=thickness, fill="",  smooth=False)
        else:
            for i in range((len(points) // 2) - 1):
                j = i * 2
                canvas.create_line(points[j], points[j + 1], points[j + 2], points[j + 3], fill=foreground, width=thickness)


def clear(mg_window):
    canvas = mg_window.get_canvas()
    background = get_param(mg_window, "background")
    canvas.config(background = background)
    for item_id in canvas.find_all():
        canvas.delete(item_id)


def make_color_rgb(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'


def mainloop(mg_window):
    """Nutno zavolat nakonec programu v případech,
        kdy se pracuje s mikrografikou mimo prostředí IDLE."""
    mg_window.get_top().mainloop()



# Test, zda je bod v polygonu.
def scalar_product(v1, v2):
    return (v1[0] * v2[0]) + (v1[1] * v2[1])


def scalar_mult(k, v):
    return list(map(lambda x: k * x, v))


def vec_plus(v1, v2):
    return list(map(lambda x,y: x + y, v1, v2))
                

def vec_minus(v1, v2):
    return list(map(lambda x,y: x - y, v1, v2))


def vec_sq_len(v):
    return scalar_product(v, v)


def is_vec_near(v1, v2, tolerance):
    return vec_sq_len(vec_minus(v1, v2)) <= (tolerance ** 2)


def is_pt_in_seg(pt, x1, x2, tolerance):
    """Rozhodne, zda je bod pt na usecnce [x1, x2]."""
    print(pt, x1, x2, tolerance)
    u = vec_minus(x2, x1)
    v = vec_minus(x1, pt)
    uu = scalar_product(u, u)
    if uu == 0:
        return is_vec_near(pt, x1, tolerance)
    else:
        k = -(scalar_product(u, v) / uu)
        return 0 <= k <= 1 and is_vec_near(pt, vec_plus(x1, scalar_mult(k, u)), tolerance)


def is_point_in_segs(pt, tolerance, points):
    for i in range(len(points)-1):
        pt1 = points[i]
        pt2 = points[i + 1]
        if is_pt_in_seg(pt, pt1, pt2, tolerance):
            return True
    return False


def is_vert_between(pt, pt1, pt2):
    pty = pt[1]
    pt1y = pt1[1]
    pt2y = pt2[1]
    return (pt1y < pty < pt2y) or (pt1y > pty > pt2y) or ((pt1y != pt2y) and ((min(pt1y, pt2y) == pty)))
    

def is_horiz_right(pt, pt1, pt2):
    ptx, pty = pt
    pt1x, pt1y = pt1
    pt2x, pt2y = pt2
    return ((pt1x - pt2x) * ((pty - pt2y) / (pt1y - pt2y)) + pt2x) < ptx


def intersects(pt, pt1, pt2):
    return is_vert_between(pt, pt1, pt2) and is_horiz_right(pt, pt1, pt2)


def count_intersections(pt, points):
    counter = 0
    for i in range(len(points) - 1):
        pt1 = points[i]
        pt2 = points[i + 1]
        if intersects(pt, pt1, pt2):
            counter += 1
    return counter


def is_point_in_poly(pt, points):
    return count_intersections(pt, points) % 2 == 1


def get_point_x_y(point):
    return [point.get_x(), point.get_y()]


def is_point_in_polygon(x, y, closed, filled, thickness, coordinates):
    point = [x, y]
    points = []
    for i in range(len(coordinates) // 2):
        points += [[coordinates[i * 2], coordinates[(i * 2) + 1]]]
    if closed or filled:
        points = [points[-1]] + points
    if filled:
        return is_point_in_poly(point, points)
    else:
        return is_point_in_segs(point, thickness, points)
