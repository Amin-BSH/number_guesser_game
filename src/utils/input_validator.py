def validate_input(prompt: str) -> bool:
    """validate if the prompt is digit or not and if the prompt is in the range of 1 to 100

    Args:
        prompt (str): prompt

    Returns:
        bool: True or False depends on the conditions
    """
    prompt_int = int(prompt)
    if prompt_int > 100 or prompt_int < 1:
        print("❌ Oops! Your number is not in the magical range of 1 to 100. Try again! 🧙‍♂️")
        return False
    else:
        return True


if __name__ == "__main__":
    validate_input("-122")
