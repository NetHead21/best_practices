def upper_everything(elements) -> list[str]:
    return [element.upper() for element in elements]


def upper_everything(elements: list[str]) -> list[str]:
    return [element.upper() for element in elements]


loud_list: list[str] = upper_everything(["Juniven", "James", "John"])
loud_list2: list[str] = upper_everything(["Ellen", "Elsie", "Elise"])

print(loud_list)
print(loud_list2)
