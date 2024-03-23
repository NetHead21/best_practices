def is_bob(name: str) -> bool:
    return name.lower == "bob"


def is_adult(age: int, has_id: bool) -> bool:
    return age >= 21 and has_id


def enter_club(name: str, age: int, has_id: bool) -> None:
    if is_bob(name):
        print("Get our of here Bob, we don't want no trouble.")
        return

    print(
        "You may enter the club."
        if is_adult(age, has_id)
        else "You may not enter the club."
    )


def main() -> None:
    enter_club("Bob", 29, has_id=True)
    enter_club("James", 29, has_id=True)
    enter_club("Sandra", 29, has_id=False)
    enter_club("Mario", 29, has_id=True)


if __name__ == "__main__":
    main()
