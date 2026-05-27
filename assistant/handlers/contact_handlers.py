from assistant.contacts.record import Record
from assistant.utils.decorators import input_error
from assistant.utils.table_printer import format_contact, format_contacts_table
from assistant.contacts.address_book import AddressBook


@input_error
def contact_add(args, book):
    try:
        name, phone, *_ = args
    except ValueError:
        raise ValueError("Give me name and phone please")

    record = book.find(name)

    if record is None:
        record = Record(name)
        book.add_record(record)

    record.add_phone(phone)

    return "Contact added."


def contact_change(*args):
    return "Command 'contact_change' TO BE IMPLEMENTED"


def contact_delete(*args):
    return "Command 'contact_delete' TO BE IMPLEMENTED"


@input_error
def contact_search(args, book: AddressBook) -> str:
    if not book.data:
        return "No contacts."
    return format_contacts_table(list(book.data.values()))


@input_error
def contact_search_name(args, book: AddressBook) -> str:
    try:
        name, *_ = args
    except ValueError:
        raise ValueError("Give me name please")

    record = book.find(name)
    if record is None:
        raise ValueError(f"Contact '{name}' not found.")
    return format_contact(record)


def contact_phone_add(*args):
    return "Command 'contact_phone_add' TO BE IMPLEMENTED"


def contact_phone_change(*args):
    return "Command 'contact_phone_change' TO BE IMPLEMENTED"


def contact_phone_delete(*args):
    return "Command 'contact_phone_delete' TO BE IMPLEMENTED"


@input_error
def contact_phone_search(args, book: AddressBook) -> str:
    return "Command 'contact_phone_search' TO BE IMPLEMENTED"


@input_error
def contact_email_add(args, book: AddressBook):
    try:
        name, email, *_ = args
    except ValueError:
        raise ValueError("Give me name and email please")

    record = book.find(name)

    if record is None:
        record = Record(name)
        book.add_record(record)

    record.add_email(email)
    return "Email added."


def contact_email_change(*args):
    return "Command 'contact_email_change' TO BE IMPLEMENTED"


def contact_email_delete(*args):
    return "Command 'contact_email_delete' TO BE IMPLEMENTED"


def contact_email_search(*args):
    return "Command 'contact_email_search' TO BE IMPLEMENTED"


def contact_birthday_set(*args):
    return "Command 'contact_birthday_set' TO BE IMPLEMENTED"


def contact_birthday_change(*args):
    return "Command 'contact_birthday_change' TO BE IMPLEMENTED"


def contact_birthday_delete(*args):
    return "Command 'contact_birthday_delete' TO BE IMPLEMENTED"


def contact_birthday_search(*args):
    return "Command 'contact_birthday_search' TO BE IMPLEMENTED"


@input_error
def contact_address_set(args, book: AddressBook):
    try:
        name, *parts = args
    except ValueError:
        raise ValueError("Give me name and address please")

    record = book.find(name)

    if record is None:
        record = Record(name)
        book.add_record(record)

    record.set_address(" ".join(parts))
    return "Address updated."


def contact_address_change(*args):
    return "Command 'contact_ddress_change' TO BE IMPLEMENTED"


def contact_address_delete(*args):
    return "Command 'contact_address_delete' TO BE IMPLEMENTED"


def contact_address_search(*args):
    return "Command 'contact_address_search' TO BE IMPLEMENTED"
