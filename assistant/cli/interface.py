from assistant.cli.parser import parse_input
from assistant.cli.commands import COMMANDS
from assistant.storage.pickle_storage import load_data, save_data


def run_cli():
    book = load_data()

    print("Welcome to assistant bot!")

    try:
        while True:
            user_input = input("Enter a command: ")

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
