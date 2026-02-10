import math


class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def sum(self, x, y, z):
        return self.x + x, self.y + y, self.z + z

    def difference(self, x, y, z):
        return self.x - x, self.y - y, self.z - z

    def scalar_multiplication(self, x, y, z):
        return (self.x * x) + (self.y * y) + (self.z * z)

    def length(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))

    def angle(self, x, y, z):
        first_vector_length = self.length()
        second_vector_length = self.length()
        vectors_scalar_multiplication = self.scalar_multiplication(x, y, z)

        res_angle = vectors_scalar_multiplication / (first_vector_length * second_vector_length)

        return res_angle



vector1 = Vector(5, 3, 1)
vector2 = Vector(5, 3, 1)

print(vector1.length())
print(vector1.difference(vector2.x, vector2.y, vector2.z))
print(vector1.angle(vector2.x, vector2.y, vector2.z))
