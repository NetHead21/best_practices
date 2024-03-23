from dataclasses import dataclass


@dataclass
class Questions:
    """
    Base class for the questions.
    """

    _no_of_questions: int = 0

    @property
    def questions(self) -> int:
        """
        Get the number of questions.

        Returns:
            int: The number of questions.
        """
        return self._no_of_questions

    @questions.setter
    def questions(self, value: int) -> None:
        """
        Set the number of questions.

        Args:
            value (int): The number of questions to set.
        """
        if value < 1:
            self._no_of_questions = 1
        elif value > 10:
            self._no_of_questions = 10
        else:
            self._no_of_questions = value
