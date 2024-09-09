import tkinter

class MGWindow:
    def __init__(self, click_handler=None):
        top = tkinter.Tk()
        top.title("micro_graphics window")
        canvas = tkinter.Canvas(top, width=297, height=210)
        canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
        if click_handler:
            canvas.bind('<1>', lambda event:click_handler(event.x, event.y))
        self.top = top
        self.canvas = canvas
        self.params = {"foreground": "black", "background": "white", "thickness": "1", "filled": False, "closed": True}

    def get_top(self):
        return self.top

    def get_canvas(self):
        return self.canvas

    def get_params(self):
        return self.params
    
def display_window(click_handler=None):
    return MGWindow(click_handler)

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

"""    
w = display_window(lambda x,y: draw_circle(w, x, y, 20))
set_param(w, "background", "yellow")
clear(w)

draw_polygon(w, [[10, 10], [100, 10], [10, 100]])
set_param(w, "filled", False)
set_param(w, "foreground", "red")
set_param(w, "closed", False)
draw_polygon(w, [[10, 10], [100, 10], [10, 100]])
"""


# Převzato z materiálů Michala Krupky k předmětu Paradigmata programování 3.
# Pouze přeloženo z Common Lispu do Pythonu.

def make_color_rgb(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'
