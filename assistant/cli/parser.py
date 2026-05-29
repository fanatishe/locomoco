import shlex


def parse_input(user_input):
    try:
        return shlex.split(user_input.strip())
    except ValueError as e:
        print(f"\n[!] Input Error: {e}. Please ensure all quotes are closed.")
        return []
