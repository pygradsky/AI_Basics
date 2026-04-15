class Game:
    CORN_PRICE: float = 5.0
    COW_PRICE: float = 45.0
    

    def __init__(self, balance=100.0):
        self.balance = balance
    
    @staticmethod
    def validate_balance(balance: float, item_price: float):
        if balance - item_price < 0:
            return False
        return True

    def buy(self, type: str, amount: int = 1):
        # Cow
        if type == "cow":
            item_price = Game.COW_PRICE * amount

            if Game.validate_balance(self.balance, item_price):
                self.balance -= item_price
                print(f"Вы купили корову за {item_price} монет. Баланс: {self.balance}")
            else:
                print("На балансе не достаточно средств!")
        # Sheep
        elif type == "sheep":
            pass
        # Corn
        elif type == "corn":
            item_price = Game.CORN_PRICE * amount

            if Game.validate_balance(self.balance, item_price):
                self.balance -= item_price
                print(f"Вы купили зерно за {item_price} монет. Баланс: {self.balance}")
            else:
                print("На балансе не достаточно средств!")
                

game = Game()
game.buy("cow", 2)
game.buy("corn")

print(game.balance)
