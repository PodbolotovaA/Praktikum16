class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def Re_x(self):
        return self.x

    def Re_y(self):
        return self.y

    def Re_width(self):
        return self.width

    def Re_height(self):
        return self.height

    def Rectangle_info(self):
        return f'{self.Re_x()}, {self.Re_y()}, {self.Re_width()}, {self.Re_height()}'
rect_1 = Rectangle(1,2,3,4)
print('Rectangle (', rect_1.Rectangle_info(), ')')

class Circle:
    def __init__(self, r):
        self.r = r

    def Ci_r(self):
        return self.r

    def Circle_info(self):
        return f'{self.Ci_r()}'
circle_1 = Circle(5)
print('Circle (', circle_1.Circle_info(), ')')