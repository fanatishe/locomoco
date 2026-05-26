from ..domain import AddressBook
from .decorators import input_error


@input_error
def add_contact(args: list[str], book: AddressBook) -> str:
    ...


@input_error
def change_contact(args: list[str], book: AddressBook) -> str:
    ...


@input_error
def show_phone(args: list[str], book: AddressBook) -> str:
    ...


@input_error
def show_all(args: list[str], book: AddressBook) -> str:
    ...


@input_error
def add_birthday(args: list[str], book: AddressBook) -> str:
    ...


@input_error
def show_birthday(args: list[str], book: AddressBook) -> str:
    ...


@input_error
def birthdays(args: list[str], book: AddressBook) -> str:
    ...


@input_error
def delete_contact(args: list[str], book: AddressBook) -> str:
    ...


@input_error
def fill_mock(args: list[str], book: AddressBook) -> str:
    ...
