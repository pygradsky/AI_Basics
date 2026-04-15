class Product:
    def init(self, name, price, delivery):
        self.name = name
        self.price = price
        self.delivery = delivery

    def cost(self):
        return self.price + self.delivery

    def info(self):
        print(self.name, "-", self.cost())


class Food(Product):
    def init(self, name, price, delivery, weight):
        super().init(name, price, delivery)
        self.weight = weight


class Electronics(Product):
    def init(self, name, price, delivery, warranty):
        super().init(name, price, delivery)
        self.warranty = warranty


class Clothes(Product):
    def init(self, name, price, delivery, size):
        super().init(name, price, delivery)
        self.size = size


class Cart:
    def init(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def total_cost(self):
        total = 0
        for p in self.products:
            total += p.cost()
        return total

    def show(self):
        for p in self.products:
            p.info()
        print("Итого:", self.total_cost())


p1 = Food("Хлеб", 50, 10, 0.5)
p2 = Electronics("Телефон", 20000, 500, 12)
p3 = Clothes("Футболка", 1500, 200, "M")

cart = Cart()

cart.add(p1)
cart.add(p2)
cart.add(p3)

cart.show()
    