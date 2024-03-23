import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = "!@#$%^&*()*+-="

character_list = letters + numbers + symbols


def generate_random_char() -> str:
    return random.choice(character_list)


def generate_password(password_len: int) -> str:
    return "".join(generate_random_char() for _ in range(password_len))


password_len = int(input("How many password characters you want?: "))
generated_password = generate_password(password_len)
print(generated_password)
