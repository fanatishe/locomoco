from ..domain import AddressBook
from .decorators import unexpected_exit
from .parser import parse_input
from .welcome import welcome
from .handlers import HANDLERS

@unexpected_exit
def run(book: AddressBook) -> None:
    welcome()
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Bye")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command in HANDLERS.keys():
            handler = HANDLERS[command]
            handler(book, *args)
        
        else:
            print("Invalid command.")
