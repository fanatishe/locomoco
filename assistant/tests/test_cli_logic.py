import sys
import os

# Force Python to find the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from assistant.cli.dispatcher import guess_command
from assistant.cli.parser import parse_input
from assistant.cli.commands import commands_list


def test_cli():
    print("\n=== CLI Logic & Parsing ===")

    # 1. Shlex parsing (Handling spaces in quotes)
    print("\n--- Parser (Multi-word strings) ---")
    raw_input = 'contact add "John Doe" 0501234567'
    parsed = parse_input(raw_input)
    print(f"Raw Input:  {raw_input}")
    print(f"Parsed List: {parsed}")
    if len(parsed) == 3 and parsed[1] == "John Doe":
        print("-> Parser successfully grouped 'John Doe' as one argument.")

    # 2. Command Guessing (Fuzzy Search)
    print("\n--- Command Guessing ---")
    # Simulate user typos
    typos = ["helpp", "contct add", "alll", "noote searh"]
    cmds = list(commands_list.keys())

    for typo in typos:
        suggestion = guess_command(typo, cmds)
        # We use .strip() because your function returns a newline at the end
        print(f"User typed: '{typo}' -> AI Suggests: {suggestion.strip()}")


if __name__ == "__main__":
    test_cli()
