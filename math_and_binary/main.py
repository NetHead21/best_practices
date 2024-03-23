from business_logic.game_tasks import get_user_score, update_user_score
from business_logic.binary_game_class import BinaryGame
from business_logic.math_game_class import MathGame
from persistence.file_operation import user_data
from presentation.user_prompt import choose_game, get_number_questions, play_again


def main():
    file_name = "user_scores.txt"
    binary_game = BinaryGame()
    math_game = MathGame()

    games = {
        1: math_game,
        2: binary_game,
    }

    user_name = input("What is your name?: ").lower()
    user = user_data(user_name, 0)
    user_score = get_user_score(file_name, user)
    score = 0

    while True:
        game_chosen = choose_game()
        game = games[game_chosen]
        number_of_questions = get_number_questions()
        game.questions = number_of_questions
        print(game)
        score += game.generate_questions()
        print(f"Your current score is: {score}")

        if not play_again():
            break

    if score > user_score:
        update_user_score(file_name, user_data(user_name, score))

    print("Thank you for playing.")


if __name__ == "__main__":
    main()
