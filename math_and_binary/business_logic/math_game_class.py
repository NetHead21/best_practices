import random

from business_logic.questions_class import Questions
from business_logic.game_class import Game
from presentation.user_input import get_user_input


class MathGame(Questions, Game):
    def _print_feed_back(self, feed_back: str, answer: int) -> None:
        print(f"{feed_back} the answer is {answer}")

    def _check_answer(self, correct_answer: int, user_answer: int) -> bool:
        is_correct = correct_answer == user_answer
        message = "Correct!" if is_correct else "Wrong!"
        self._print_feed_back(message, correct_answer)
        return is_correct

    def _get_score(self, raw_question: int | str) -> int:
        while True:
            question = (
                f"What is the result of {raw_question}? {int(eval(raw_question))}"
            )
            try:
                answer = int(get_user_input(question))
                return 1 if self._check_answer(int(eval(raw_question)), answer) else 0
            except ValueError:
                print("Invalid Input! Please type a integer number only.")

    def get_question(self) -> str:
        operators = ["+", "-", "*", "/"]
        number_list = [str(self.get_random_number(1, 9)) for _ in range(5)]
        symbol_list = [random.choice(operators) for _ in range(5)]

        # items = []
        # for pair in zip(number_list, symbol_list):
        #     items.extend(iter(pair))

        # question_list= [item for pair in zip(number_list, symbol_list) for item in pair]
        # question_string = " ".join(question_list)

        return " ".join(
            [item for pair in zip(number_list, symbol_list) for item in pair][:-1]
        )

    def generate_questions(self):
        # score = 0
        # for _ in range(self.questions):
        #     question = self.get_question()
        #     score += self._get_score(question)
        # return score

        return sum(self._get_score(self.get_question()) for _ in range(self.questions))

    def __str__(self):
        return """
MATH GAME INSTRUCTIONS:
In this game, you will be given a simple arithmetic question.
Each correct answer gives you one mark.
No mark is deducted for wrong answers.\n"""


if __name__ == "__main__":
    game = MathGame()
    print(game)
    game.questions = 2
    score = game.generate_questions()
    print(score)
