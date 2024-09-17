from src.utils.input_validator import validate_input
from src.game_logic.generate_random_number import random_number_generator
from src.game_logic.hint_function import show_hint
from game_logic.scorer import Scorer


if __name__ == "__main__":
    starter_number = 1
    ender_number = 100
    random_number = random_number_generator(start=starter_number, end=ender_number)
    scorer = Scorer()

    while True:
        guessed_number = input(
            f"🔢 Go ahead, take your best shot! Enter a number between {starter_number if starter_number else 1} and {ender_number if ender_number else 100} (or 'q' to exit): "
        ).lower()

        if guessed_number == "q":
            print(
                "🚪 Exiting the game? No worries! Your secret number awaits next time."
            )
            print(f"🎯 Your final score: {scorer.return_score()}")
            break
        elif not guessed_number.isdigit():
            print(
                "❌ Oops! That's not a valid number. Try again with a whole number, my friend!"
            )
            continue
        else:
            validation_of_input = validate_input(guessed_number)
            if validation_of_input:
                if int(guessed_number) == random_number:
                    print(
                        f"🎉 Bingo! You've cracked the code! The secret number was {random_number}. 🎉"
                    )
                    print(f"🏆 Your score is: {scorer.return_score()}")
                    break
                else:
                    show_hint(
                        random_number=random_number, guessed_number=guessed_number
                    )
                    scorer.decrement_score()
                    print(f"Your score is: {scorer.return_score()}")
                    if scorer.return_score() == 0:
                        print("🔥 Game over! Your score has hit rock bottom.")
                        print(f"The random number was {random_number}")
                        break
            else:
                continue
