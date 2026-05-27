from ..domain import AddressBook, Record
from .decorators import input_error


@input_error
def add_contact(args: list[str], book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)

    if record is None:
        record = Record(name)
        book.add_record(record)

    if len(args) > 1:
        record.add_phone(args[1])

    book.save()
    return "Contact added."


@input_error
def change_contact(args: list[str], book: AddressBook) -> str:
    name = args[0]
    field = args[1]
    value = " ".join(args[2:])

    record = book.find(name)

    if record is None:
        return "Contact not found."

    if field == "phone":
        record.phones.clear()
        record.add_phone(value)

    elif field == "email":
        record.edit_email(value)

    elif field == "address":
        record.edit_address(value)

    elif field == "birthday":
        record.add_birthday(value)

    else:
        return "Unknown field. Use: phone, email, address, birthday."

    book.save()
    return "Contact updated."


@input_error
def show_phone(args: list[str], book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)

    if record is None:
        return "Contact not found."

    phones = "; ".join(str(phone) for phone in record.phones)

    return phones if phones else "No phones."


@input_error
def show_all(args: list[str], book: AddressBook) -> str:
    return str(book)


@input_error
def add_birthday(args: list[str], book: AddressBook) -> str:
    name = args[0]
    birthday = args[1]

    record = book.find(name)

    if record is None:
        return "Contact not found."

    record.add_birthday(birthday)
    book.save()

    return "Birthday added."


@input_error
def show_birthday(args: list[str], book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)

    if record is None:
        return "Contact not found."

    if record.birthday is None:
        return "Birthday not added."

    return str(record.birthday)


@input_error
def birthdays(args: list[str], book: AddressBook) -> str:
    result = book.get_upcoming_birthdays()

    if not result:
        return "No upcoming birthdays."

    return "\n".join(str(item) for item in result)


@input_error
def delete_contact(args: list[str], book: AddressBook) -> str:
    name = args[0]

    book.delete(name)
    book.save()

    return "Contact deleted."


@input_error
def add_note(args: list[str], book: AddressBook) -> str:
    name = args[0]
    text = " ".join(args[1:])

    if not text:
        return "Enter note text."

    record = book.find(name)

    if record is None:
        return "Contact not found."

    record.add_note(text)
    book.save()

    return "Note added."


@input_error
def list_notes(args: list[str], book: AddressBook) -> str:
    name = args[0]

    record = book.find(name)

    if record is None:
        return "Contact not found."

    return record.list_notes()


@input_error
def edit_note(args: list[str], book: AddressBook) -> str:
    name = args[0]
    index = int(args[1])
    text = " ".join(args[2:])

    if not text:
        return "Enter new note text."

    record = book.find(name)

    if record is None:
        return "Contact not found."

    record.edit_note(index, text)
    book.save()

    return "Note updated."


@input_error
def delete_note(args: list[str], book: AddressBook) -> str:
    name = args[0]
    index = int(args[1])

    record = book.find(name)

    if record is None:
        return "Contact not found."

    record.delete_note(index)
    book.save()

    return "Note deleted."


@input_error
def delete_notes_by_name(args: list[str], book: AddressBook) -> str:
    name = args[0]

    record = book.find(name)

    if record is None:
        return "Contact not found."

    record.delete_all_notes()
    book.save()

    return "All notes deleted."


@input_error
def fill_mock(args: list[str], book: AddressBook) -> str:
    record = Record("John")
    record.add_phone("0501234567")
    record.add_email("john@gmail.com")
    record.add_address("Kyiv")
    record.add_birthday("01.01.2000")
    record.add_note("Test note")

    book.add_record(record)
    book.save()

    return "Mock data added."
