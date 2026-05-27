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
def set_address(args, book: AddressBook):
    name, *parts = args
    if not parts:
        raise ValueError("Address cannot be empty.")

    record = book.find(name)

    if record is None:
        record = Record(name)
        book.add_record(record)

    record.set_address(" ".join(parts))
    return "Address updated."


@input_error
def set_note(args, book: AddressBook):
    name, *parts = args
    if not parts:
        raise ValueError("Note cannot be empty.")

    record = book.find(name)

    if record is None:
        record = Record(name)
        book.add_record(record)

    record.set_note(" ".join(parts))
    return "Note updated."


@input_error
def add_email(args, book: AddressBook):
    if len(args) != 2:
        raise ValueError("Usage: add-email <name> <email>")
    name, email = args

    record = book.find(name)

    if record is None:
        record = Record(name)
        book.add_record(record)

    record.add_email(email)
    return "Email added."


@input_error
def show_all(args, book: AddressBook) -> str:
    if not book.data:
        return "No contacts."
    return format_contacts_table(list(book.data.values()))


def contact_add():
    print("Command 'contact_add' TO BE IMPLEMENTED")


def contact_change():
    print("Command 'contact_change' TO BE IMPLEMENTED")


def contact_delete():
    print("Command 'contact_delete' TO BE IMPLEMENTED")


def contact_search():
    print("Command 'contact_search' TO BE IMPLEMENTED")


def contact_phone_add():
    print("Command 'contact_phone_add' TO BE IMPLEMENTED")


def contact_phone_change():
    print("Command 'contact_phone_change' TO BE IMPLEMENTED")


def contact_phone_delete():
    print("Command 'contact_phone_delete' TO BE IMPLEMENTED")


def contact_phone_search():
    print("Command 'contact_phone_search' TO BE IMPLEMENTED")


def contact_email_add():
    print("Command 'contact_email_add' TO BE IMPLEMENTED")


def contact_email_change():
    print("Command 'contact_email_change' TO BE IMPLEMENTED")


def contact_email_delete():
    print("Command 'contact_email_delete' TO BE IMPLEMENTED")


def contact_email_search():
    print("Command 'contact_email_search' TO BE IMPLEMENTED")


def contact_birthday_set():
    print("Command 'contact_birthday_set' TO BE IMPLEMENTED")


def contact_birthday_change():
    print("Command 'contact_birthday_change' TO BE IMPLEMENTED")


def contact_birthday_delete():
    print("Command 'contact_birthday_delete' TO BE IMPLEMENTED")


def contact_birthday_search():
    print("Command 'contact_birthday_search' TO BE IMPLEMENTED")


def contact_address_set():
    print("Command 'contact_address_set' TO BE IMPLEMENTED")


def contact_address_change():
    print("Command 'contact_ddress_change' TO BE IMPLEMENTED")


def contact_address_delete():
    print("Command 'contact_address_delete' TO BE IMPLEMENTED")


def contact_address_search():
    print("Command 'contact_address_search' TO BE IMPLEMENTED")
