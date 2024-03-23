from persistence.file_operation import get_file_data, remove_file, post_data
from persistence.file_operation import user_data


def get_user_score(file_name: str, user: user_data) -> int:
    """
    Retrieves the score of the specified user from the given file.

    Args:
        file_name (str): The name of the file containing the user scores.
        user (user_data): The name of the user to retrieve the score for.

    Returns:
        int: The score of the specified user, or "User Does Not Exist!" if the user is not found.
    """
    users_data = get_file_data(file_name)
    return int(users_data.get(user.name, 0))


def update_user_score(file_name: str, user: user_data) -> None:
    """
    Updates the score of the specified user in the given file.

    Args:
        file_name (str): The name of the file containing the user scores.
        user (str): The name of the user to update the score for.
        score (int): The new score to assign to the user.
    """
    users_score = get_file_data(file_name)
    users_score[user.name] = user.score
    remove_file(file_name)
    for data in users_score.items():
        post_data(file_name, user_data(*data))
