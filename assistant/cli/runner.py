from ..domain import AddressBook
from .decorators import unexpected_exit
from .parser import parse_input
from .welcome import welcome

@unexpected_exit
def run(book: AddressBook) -> None:
    welcome()
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            ...

        elif command == "change":
            ...

        elif command == "del":
            ...

        elif command == "phone":
            ...

        elif command == "all":
            ...

        elif command == "add-birthday":
            ...

        elif command == "show-birthday":
            ...

        elif command == "birthdays":
            ...

        elif command == "fill-mock":
            ...
        else:
            print("Invalid command.")
