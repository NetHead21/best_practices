import time


def connect() -> None:
    print("Connecting to the internet")
    time.sleep(3)
    print("You are connected!")


if __name__ == "__main__":
    connect()