from ..domain import AddressBook
from .decorators import input_error


@input_error
def add_contact(book: AddressBook, args: list[str]) -> str:
    ...

@input_error
def change_contact(book: AddressBook, args: list[str]) -> str:
    ...
    
@input_error
def find_contact(book: AddressBook, args: list[str]) -> str:
    ...

@input_error
def show_phone(book: AddressBook, args: list[str]) -> str:
    ...

@input_error
def show_all(book: AddressBook, args: list[str]) -> str:
    ...

@input_error
def add_birthday(book: AddressBook, args: list[str]) -> str:
    ...

@input_error
def show_birthday(book: AddressBook, args: list[str]) -> str:
    ...

@input_error
def birthdays(book: AddressBook, args: list[str]) -> str:
    ...

@input_error
def delete_contact(book: AddressBook, args: list[str]) -> str:
    ...

@input_error
def fill_mock(book: AddressBook, args: list[str]) -> str:
    ...


HANDLERS = {
    "add": add_contact,
    "change": change_contact,
    "delete": delete_contact,
    "find": find_contact,
    "phone": show_phone,
    "all": show_all,
    "add-birthday": add_birthday,
    "show-birthday": show_birthday,
    "birthdays": birthdays,
    "fill-mock": fill_mock,
}
