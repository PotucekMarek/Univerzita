import math

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_x(self, x):
        self.x = x
        return self
    
    def set_y(self, y):
        self.y = y
        return self

class Circle:
    def __init__(self):
        self.center = Point()
        self.radius = 1
        
    def get_radius(self):
        return self.radius
    
    def set_radius(self, radius):
        self.radius = radius
        return self
    
    def get_center(self):
        return self.center

class Ellipse:
    def __init__(self):
        self.focal_point1 = Point()
        self.focal_point2 = Point()
        self.major_semiaxis = 1

    def get_center(self):
        self.center = Point()
        self.set_center_f1 = ((self.focal_point1.get.x)+(self.focal_point2.get.x))/2
        self.set_center_f2 = ((self.focal_point1.get.y)+(self.focal_point2.get.y))/2
        return self.center
    

        

