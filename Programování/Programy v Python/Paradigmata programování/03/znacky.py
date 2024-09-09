from omg_03 import *

def make_points(coords_array):
    points = []
    for coords in coords_array:
        point = Point().move(coords[0], coords[1])
        points += [point]
    return points

def make_sign_items():
    poly1 = Polygon()
    poly2 = Polygon()
    poly_line1 = Polygon()
    poly_line2 = Polygon()
    poly_line3 = Polygon()
    poly_line4 = Polygon()
    poly_line5 = Polygon()

    poly1.set_vertices(make_points([[55, 158], [150, 5],[245, 158]]))
    poly1.set_thickness(2)

    poly2.set_vertices(make_points([[80, 145], [150, 30],[220, 145]]))
    poly2.set_color("firebrick2")
    poly2.set_thickness(20)

    poly_line1.set_vertices(make_points([[150, 90], [165, 110]]))
    poly_line1.set_thickness(6)

    poly_line2.set_vertices(make_points([[150, 90], [135, 110]]))
    poly_line2.set_thickness(6)

    poly_line3.set_vertices(make_points([[150, 130], [165, 110]]))
    poly_line3.set_thickness(6)

    poly_line4.set_vertices(make_points([[135, 110], [150, 130]]))
    poly_line4.set_thickness(6)

    poly_line5.set_vertices(make_points([[150, 103], [150, 117]]))
    poly_line5.set_thickness(6)
    return [poly1, poly2, poly_line1, poly_line2,poly_line3, poly_line4, poly_line5]

def make_sign():
    return Picture().set_items(make_sign_items())

def display_sign_window():
    return Window().set_background("white").set_shape(make_sign()).redraw()

w = display_sign_window()

a = input()

