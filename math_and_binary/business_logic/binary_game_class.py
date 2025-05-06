from business_logic.game_class import Game
from business_logic.questions_class import Questions
from presentation.user_input import get_user_input


class BinaryGame(Questions, Game):
    def _print_feed_back(self, feed_back: str, answer: int) -> None:
        print(f"{feed_back} the binary equivalent of {answer} is {answer:b}")

    def _check_answer(self, correct_answer: int, user_answer: int) -> bool:
        is_correct = correct_answer == user_answer
        message = "Correct!" if is_correct else "Wrong!"
        self._print_feed_back(message, correct_answer)
        return is_correct

    def _get_score(self, raw_question: int | str) -> int:
        while True:
            question = (
                f"What is the binary equivalent of {raw_question}? {raw_question:b}"
            )
            try:
                answer = int(get_user_input(question), base=2)
                return 1 if self._check_answer(raw_question, answer) else 0
            except ValueError:
                print("Invalid Input! Please type a binary number only.")

    def generate_questions(self):
        # score = 0
        # for _ in range(self.questions):
        #     base_10 = get_random_number()
        #     score += self._get_score(base_10)
        #
        # return score
        return sum(
            self._get_score(self.get_random_number(1, 101))
            for _ in range(self.questions)
        )

    def __str__(self):
        return """
BINARY GAME INSTRUCTIONS:
In this game, you will be given a number in base 10.
Your task is to convert this number to base 2.
Each correct answer gives you one mark.
No mark is deducted for wrong answers.\n"""


if __name__ == "__main__":
    game = BinaryGame()
    print(game)
    game.questions = 3
    score = game.generate_questions()
    print(score)
