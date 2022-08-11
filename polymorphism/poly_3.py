class Shape():
    def __init__(self, area, radius, length, breadth):
        self.area = area
        self.radius = radius
        self.length = length
        self.breadth = breadth

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
    def printcirclevolume(self):
        print(f"the radius is {self.radius} and the volume is {3.14*self.radius**2}")


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def printrectanglevolume(self):
        print(f"the volume of rectangle is {self.length * self.breadth}")


class Square(Shape):
    def __init__(self, area):
        self.area = area
    def printsquarevolume(self):
        print(f"the volume of square is {self.area ** 2}")

s1 = Circle(25)
s1.printcirclevolume()
s2 = Rectangle(4, 5)
s2.printrectanglevolume()
s3 = Square(20)
s3.printsquarevolume()