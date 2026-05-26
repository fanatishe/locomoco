from assistant.contacts.record import Record
from assistant.utils.decorators import input_error


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
def show_all(args, book):
    if not book.data:
        return "No contacts."

    return "\n".join(str(record) for record in book.data.values())
