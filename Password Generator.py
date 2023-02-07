import random
import string


def generate_password(length):
    letters_and_digits = string.ascii_letters + string.digits
    password = "".join(random.choice(letters_and_digits)
                       for i in range(length))
    return password


length = int(input("Enter the password length: "))
password = generate_password(length)
print("Generated password:", password)
