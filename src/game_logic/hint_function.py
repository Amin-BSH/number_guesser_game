def show_hint(random_number: int, guessed_number: str) -> None:
    """show hints to the player

    Args:
        random_number (int)
        guessed_number (int)
    """
    guessed_number_int = int(guessed_number)
    if abs(random_number - guessed_number_int) > 15:
        print("🔍 Your guess is far from the random number. Try a different number.")
    else:
        print("🔍 You're getting closer! Adjust your guess.")
