import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

character_list = letters + numbers + symbols


def generate_random_char() -> str:
    # random_num = random.randint(0, len(character_list) -1)
    # random_char = character_list[random_num]
    # random_car = random.choice(character_list)
    # return random_car
    return random.choice(character_list)


def generate_password(password_len: int) -> str:
    # password = ""

    # for i in range(password_len):
    #     password += generate_random_char()

    # return password
    return "".join(generate_random_char() for _ in range(password_len))


password_len = int(input("How many password characters do you want?: "))
new_password = generate_password(password_len)
print(new_password)
