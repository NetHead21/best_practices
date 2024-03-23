from abc import ABC, abstractmethod
from random import randint


class Game(ABC):
    @staticmethod
    def get_random_number(start: int, end: int) -> int:
        """
        Generates a random integer between 1 and 101 (inclusive).

        Returns:
            int: The generated random number.
        """
        return randint(start, end)

    @abstractmethod
    def _print_feed_back(self, feed_back: str, answer: int) -> None:
        """
        Print feedback message.

        Args:
            feed_back (str [Correct! or Wrong!]): The feedback message.
            answer (int): The answer to display in the message.
        """
        ...

    @abstractmethod
    def _check_answer(self, correct_answer: int, user_answer: int) -> bool:
        """
        Check if the user's answer is correct.

        Args:
            correct_answer (int): The correct answer.
            user_answer (int): The user's answer.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        ...

    @abstractmethod
    def _get_score(self, raw_question: int | str) -> int:
        """
        Get the score based on the user's answer.

        Args:
            raw_question (int): The problem to solve.

        Returns:
            int: The score (1 if the answer is correct, 0 otherwise).
        """
        ...

    @abstractmethod
    def generate_questions(self):
        """
        Generates questions and calculates the total score.

        Returns:
            int: The total score calculated based on the generated questions.
        """
