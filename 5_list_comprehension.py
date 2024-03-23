names: list[str] = ["Juniven", "James", "Jay", "Ellen", "Elsie", "Elise", "Charlotte"]


# long_names = []
# for name in names:
#     if len(name) > 6:
#         long_names.append(name)

# print(long_names)


long_names = [name for name in names if len(name) > 6]

print(long_names)
