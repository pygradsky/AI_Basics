import math


class Figure:
    def init(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        print("Новые координаты:", self.x, self.y)


class Circle(Figure):
    def init(self, x, y, r):
        super().init(x, y)
        self.r = r

    def resize(self, new_r):
        self.r = new_r
        print("Новый радиус:", self.r)

    def area(self):
        s = math.pi * self.r ** 2
        print("Площадь круга:", s)


class Square(Figure):
    def init(self, x, y, a):
        super().init(x, y)
        self.a = a

    def resize(self, new_a):
        self.a = new_a
        print("Новая сторона:", self.a)

    def area(self):
        s = self.a ** 2
        print("Площадь квадрата:", s)


class Rectangle(Figure):
    def init(self, x, y, a, b):
        super().init(x, y)
        self.a = a
        self.b = b

    def resize(self, new_a, new_b):
        self.a = new_a
        self.b = new_b
        print("Новые стороны:", self.a, self.b)

    def area(self):
        s = self.a * self.b
        print("Площадь прямоугольника:", s)


c = Circle(0, 0, 5)
s = Square(2, 2, 4)
r = Rectangle(1, 1, 3, 6)

c.area()
c.move(1, 1)
c.resize(10)
print()

s.area()
s.move(-1, 3)
s.resize(7)
print()

r.area()
r.move(5, 5)
r.resize(2, 8)
