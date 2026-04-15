class Account:
    def init(self, owner, number, percent, open_date, balance):
        self.owner = owner
        self.number = number
        self.percent = percent
        self.open_date = open_date
        self.balance = balance

    def print_info(self):
        print("Владелец:", self.owner)
        print("Номер счета:", self.number)
        print("Процент:", self.percent, "%")
        print("Дата открытия:", self.open_date)
        print("Баланс:", self.balance, "руб")

    def change_owner(self, new_owner):
        self.owner = new_owner
        print("Новый владелец:", self.owner)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств")
        else:
            self.balance -= amount
            print("Снято:", amount)
            print("Баланс:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Добавлено:", amount)
        print("Баланс:", self.balance)

    def add_percent(self):
        profit = self.balance * self.percent / 100
        self.balance += profit
        print("Начислено:", profit)
        print("Баланс:", self.balance)

    def to_dollars(self, rate):
        dollars = self.balance / rate
        print("В долларах:", dollars)


acc = Account("Иванов", "123456", 5, "01.01.2024", 100000)

acc.print_info()
print()

acc.change_owner("Петров")
print()

acc.deposit(5000)
print()

acc.withdraw(20000)
print()

acc.add_percent()
print()

acc.to_dollars(90)
