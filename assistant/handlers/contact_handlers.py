from assistant.contacts.record import Record
from assistant.utils.decorators import input_error
from assistant.utils.table_printer import format_contact, format_contacts_table
from assistant.contacts.address_book import AddressBook


@input_error
def add_contact(args, book):
    name, phone = args

    record = book.find(name)

    if record is None:
        record = Record(name)
        book.add_record(record)

    record.add_phone(phone)

    return "Contact added."


@input_error
def show_contact(args, book: AddressBook) -> str:
    (name,) = args
    record = book.find(name)
    if record is None:
        raise ValueError(f"Contact '{name}' not found.")
    return format_contact(record)


@input_error
def show_all(args, book: AddressBook) -> str:
    if not book.data:
        return "No contacts."
    return format_contacts_table(list(book.data.values()))
