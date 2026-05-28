from ..domain import AddressBook
from .decorators import unexpected_exit
from .parser import parse_input
from .handlers import (
    add_contact,
    change_contact,
    show_phone,
    show_all,
    add_birthday,
    show_birthday,
    birthdays,
    delete_contact,
    add_note,
    list_notes,
    edit_note,
    delete_note,
    delete_notes_by_name,
    fill_mock,
)


@unexpected_exit
def run(book: AddressBook) -> None:
    book.load()

    commands = {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
        "add-birthday": add_birthday,
        "show-birthday": show_birthday,
        "birthdays": birthdays,
        "delete": delete_contact,

        "add-note": add_note,
        "notes": list_notes,
        "edit-note": edit_note,
        "delete-note": delete_note,
        "delete-notes": delete_notes_by_name,

        "fill-mock": fill_mock,
    }

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        command, args = parse_input(user_input)

        if command in ["close", "exit", "quit"]:
            print("Good bye!")
            break

        handler = commands.get(command)

        if handler is None:
            print("Invalid command.")
            continue

        result = handler(args, book)

        if result:
            print(result)
