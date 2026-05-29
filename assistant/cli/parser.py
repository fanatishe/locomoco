import shlex


def parse_input(user_input: str) -> list[str]:
    """
    Safely splits the user's raw input string into a list of arguments.

    Utilizes shlex to ensure that words wrapped in quotes (e.g., "John Doe")
    are treated as a single argument rather than split by spaces.

    Args:
        user_input (str): The raw string entered in the terminal.

    Returns:
        list[str]: A list of parsed string arguments.
    """
    try:
        return shlex.split(user_input.strip())
    except ValueError as e:
        print(f"\n[!] Input Error: {e}. Please ensure all quotes are closed.")
        return []
