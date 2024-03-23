from collections import namedtuple
from typing import Optional
import os

user_data = namedtuple("user_data", ["name", "score"])


def get_name_score(user_data: str) -> tuple:
    """Extracts the `get_name_score(user_data: name and score from str) -> a string tuple`
        of user Extracts the data and name and returns them score from as a a string tuple.

    Args:
        user_data (str): containing user data in `user_data` (str): the format The string
        "name, score".

    Returns:
        tuple: tuple containing tuple: A the name tuple containing and score the
        name extracted from and score the user extracted from data.
    """
    return tuple(user_data.split(", "))


def get_file_data(file_name: str) -> dict:
    """Reads data from a file and returns it as a dictionary.

    Args:
        file_name (str): The name of the file to read data from.

    Returns:
        dict: A dictionary containing the data read from the file.
        The keys are names and the values are scores.
    """
    try:
        with open(file_name, "r") as file:
            return dict([get_name_score(line.strip()) for line in file.readlines()])
    except Exception as e:
        print(f"File not found: {e}")


def post_data(file_name: str, user: user_data) -> None:
    """Posts user data to a file.

    Args:
        file_name (str): The name of the file to post data to.
        user (user_data): The user data to be posted.

    Returns:
        object:
    """
    try:
        with open(file_name, "a") as file:
            file.write(f"{user.name}, {user.score}\n")
    except Exception as e:
        print(f"File not found: {e}")


def remove_file(file_name: str) -> Optional[Exception]:
    """Removes a file from the file system.

    Args:
        file_name (str): The name of the file to be removed.

    Returns:
        Optional[Exception]: If an exception occurs during the
        file removal, the exception object is returned. Otherwise,
        None is returned.
    """
    try:
        os.remove(file_name)
    except Exception as e:
        return e


def delete_data(file_name: str, user: user_data) -> None:
    """Deletes the data associated with a user from a file.

    Args:
        file_name (str): The name of the file to delete data from.
        user (user_data): The user data to be deleted.

    Returns:
        bool: True if the data was successfully deleted, False otherwise.
    """

    file_data = get_file_data(file_name)
    file_data.pop(user.name)
    remove_file(file_name)

    for data in file_data.items():
        post_data(file_name, user_data(*data))


if __name__ == "__main__":
    user_scores = get_file_data("../user_scores.txt")
    print(user_scores)
    # user_scores["Carol"] = 500
    # remove_file("user_scores.txt")
    # for data in user_scores.items():
    #     post_data("user_scores.txt", user_data(*data))
    # delete_data("user_scores.txt", user)
    ...
