class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real      
        self.imag = imag
         
    def print_number(self):
        print(f"{self.real} + {self.imag}i")

    def add(self, other):
        r = self.real + other.real
        i = self.imag + other.imag
        return ComplexNumber(r, i)
    
    def sub(self, other):
        r = self.real - other.real
        i = self.imag - other.imag
        return ComplexNumber(r, i)
    
    def mul(self, other):
        r = self.real * other.real - self.imag * other.imag
        i = self.real * other.imag + self.imag * other.real
        return ComplexNumber(r, i)


z1 = ComplexNumber(7, -5)
z2 = ComplexNumber(2, -14)
print("Первое число:")
z1.print_number()
print("Второе число:")
z2.print_number()
print("\nСложение:")
z3 = z1.add(z2)
z3.print_number()
print("\nВычитание:")
z4 = z1.sub(z2)
z4.print_number()
print("\nУмножение:")
z5 = z1.mul(z2)
z5.print_number()
