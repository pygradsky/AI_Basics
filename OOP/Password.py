import string
import random


class Password:
    ASCII_LOWERCASE = string.ascii_lowercase
    ASCII_UPPERCASE = string.ascii_uppercase
    DIGITS = "0123456789"

    def __init__(self, user_password):
        if not self.check_password(user_password):
            print("Пароль не соответствует требованим!ют пароль")
            self.psw = self.generate_safety_password()
        else:
            self.psw = user_password

    def check_password(self, psw):
        if len(psw) < 10:
            return False

        has_lower = any(c in self.ASCII_LOWERCASE for c in psw)
        has_upper = any(c in self.ASCII_UPPERCASE for c in psw)
        has_digit = any(c in self.DIGITS for c in psw)

        return has_lower and has_upper and has_digit

    def generate_safety_password(self):
        characters = self.ASCII_LOWERCASE + self.ASCII_UPPERCASE + self.DIGITS

        lower = random.choice(self.ASCII_LOWERCASE)
        upper = random.choice(self.ASCII_UPPERCASE)
        digit = random.choice(self.DIGITS)

        remaining = "".join(random.choice(characters) for _ in range(random.randint(10, 20)))

        listed_password_chars = list(lower + upper + digit + remaining)
        random.shuffle(listed_password_chars)

        return "".join(listed_password_chars)


user_psw1 = Password("qwerty123456789")
user_psw2 = Password("Rectangle2026$")

print(user_psw1.psw)
print(user_psw2.psw)