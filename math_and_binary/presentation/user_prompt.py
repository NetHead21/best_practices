from presentation.user_input import get_user_input


def choose_game() -> int:
    while True:
        try:
            prompt = int(get_user_input("Math Game (1) or Binary Game (2)?"))
            if prompt not in (1, 2):
                print("Please choose between 1 and 2 only.")
                continue
            return prompt
        except ValueError:
            print("Invalid Input. Please choose between 1 and 2 only.")


def get_number_questions() -> int:
    while True:
        try:
            return int(
                get_user_input("How many questions do you want to answer? (1 to 10)")
            )
        except ValueError:
            print("Invalid Input. Please choose integer value only.")


def play_again() -> bool:
    while True:
        again = input("Do you want to play again? (Y/n): ").lower()
        if again not in ("y", "n"):
            print("Please chose between (Y/N) only.")
            continue
        return again == "y"


if __name__ == "__main__":
    # number_of_questions = get_number_question()
    # print(number_of_questions)
    # game_chosen = choose_game()
    # print(game_chosen)
    again = play_again()
    print(again)
