from assistant.contacts.address_book import AddressBook

from assistant.cli.parser import parse_input
from assistant.cli.commands import COMMANDS


def run_cli():
    book = AddressBook()

    print("Welcome to assistant bot!")

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
