import math


class KvadratnoeUravnenie:
    def init(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def print_koeff(self):
        print(f"a = {self.a}, b = {self.b}, c = {self.c}")
    def reshit(self):
        D = self.b ** 2 - 4 * self.a * self.c
        print(f"Дискриминант D = {D}")
        if D > 0:
            x1 = (-self.b + math.sqrt(D)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(D)) / (2 * self.a)
            print(f"Два корня: x1 = {x1}, x2 = {x2}")
        elif D == 0:
            x = -self.b / (2 * self.a)
            print(f"Один корень: x = {x}")
        else:
            print("Корней нет (D < 0)")


ur = KvadratnoeUravnenie(1, -3, 2)
ur.print_koeff()
ur.reshit()
