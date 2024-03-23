# numbers: list[int] = list(range(1, 11))
# text: str = "Hello, world!"

# print("Original")
# print(numbers)
# print(text)

# print()

# print("Reversed")
# print(text[::-1])
# print(numbers[::-1])

# rev: slice = slice(None, None, -1)
# f_five: slice = slice(None, 5)

# print("Reversed using slice classs")
# print(text[rev])
# print(numbers[rev])

# print("Printing the first five elments.")
# print(text[f_five])
# print(numbers[f_five])


# the walrus operator in action
# users: dict[int, str] = {
#     0: "Bob",
#     1: "Mario",
# }

# user: str | None = users.get(0)

# if user:
#     print(f"{user} is found")
# else:
#     print(f"{user} is not found!")

# if user := users.get(0):
#     print(f"{user} is found")
# else:
#     print(f"{user} is not found!")


def get_info(text: str) -> dict:
    # return {
    #     "words": text.split(),
    #     "word_count": len(text.split()),
    #     "character_count": len(text),
    # }

    return {
        "words": (words := text.split()),
        "word_count": len(words),
        "character_count": len(" ".join(words)),
    }


print(get_info("Bob"))
print(get_info("Hello World"))
print(
    get_info("The quick brown fox jumped over the lazy dog near the bank of the river.")
)

# Share also the idea of primeval whirl take a picture walrus operation
