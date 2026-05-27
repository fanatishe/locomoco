from assistant.cli.parser import parse_input
from assistant.cli.commands import COMMANDS
from assistant.storage.pickle_storage import load_data, save_data
from assistant.cli.cli_prompt import get_user_input
from assistant.utils.welcome_message import generate_jarvis_interface


def run_cli():
    generate_jarvis_interface()
    book = load_data()

    try:
        while True:
            user_input = get_user_input()

            command, args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            if command == "hello":
                print("How can I help you?")
                continue

            handler = COMMANDS.get(command)

            if handler is None:
                print("Invalid command.")
                continue

            result = handler(args, book)

            print(result)
    finally:
        save_data(book)
