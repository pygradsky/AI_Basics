import string
import random


class Password:
    ASCII_LOWERCASE = string.ascii_lowercase
    ASCII_UPPERCASE = string.ascii_uppercase
    DIGITS = "0123456789"

    def __init__(self, user_password):
        if not self.check_password(user_password):
            self.psw = self.generate_safety_password()
        else:
            self.psw = user_password

    def check_password(self, psw):
        if len(psw) >= 10 \
                and (psw.strip(self.ASCII_LOWERCASE)) \
                and (psw.strip(self.ASCII_UPPERCASE)) \
                and (psw.strip(self.DIGITS)):
            return True
        return False

    def generate_safety_password(self):
        safety_psw = ""
        while True:
            if self.check_password(safety_psw):
                return safety_psw
            else:
                safety_psw += random.choice(self.ASCII_LOWERCASE + self.ASCII_UPPERCASE + self.DIGITS)


user_psw = Password("Vangok2000")
print(user_psw.psw)
print(user_psw.generate_safety_password())
