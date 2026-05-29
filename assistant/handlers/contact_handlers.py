from assistant.contacts.record import Record
from assistant.utils.decorators import input_error
from assistant.utils.table_printer import format_contacts_table
from assistant.contacts.address_book import Book
from assistant.contacts.phone import Phone
from assistant.utils.birthday_utils import normalize_date


@input_error
def contact_add(args, book: Book):
    try:
        name, phone, *extra_args = args
    except ValueError:
        raise ValueError("Give me name and phone please")

    if name in book.addressbook.data:
        record = book.addressbook.data[name]
    else:
        record = Record(name)
        book.addressbook.add_record(record)

    record.add_phone(phone)

    if extra_args:
        standard_birthday = normalize_date(extra_args[0]).strftime("%d.%m.%Y")
        record.set_birthday(standard_birthday)

    return "Contact added."


def contact_change(*args):
    return "Command 'contact_change' TO BE IMPLEMENTED"


def contact_delete(*args):
    return "Command 'contact_delete' TO BE IMPLEMENTED"


@input_error
def contact_search(args, book: Book) -> str:
    # If no arguments are passed, show all contacts
    if not args or not args[0].strip():
        if not book.addressbook.data:
            return "No contacts found."
        return format_contacts_table(list(book.addressbook.data.values()))

    query = args[0].lower()
    matched_records = []

    for name, record in book.addressbook.data.items():
        if query in name.lower():
            matched_records.append(record)

    if not matched_records:
        return f"No contacts found matching username: '{args[0]}'"

    return format_contacts_table(matched_records)


def contact_phone_add(*args):
    return "Command 'contact_phone_add' TO BE IMPLEMENTED"


def contact_phone_change(*args):
    return "Command 'contact_phone_change' TO BE IMPLEMENTED"


def contact_phone_delete(*args):
    return "Command 'contact_phone_delete' TO BE IMPLEMENTED"


@input_error
def contact_phone_search(args, book: Book) -> str:
    if not args:
        raise ValueError("Give me a phone number to search for please")

    # Strip everything except digits from the search query
    query_digits = Phone.get_num(args[0])
    if not query_digits:
        raise ValueError("Search query must contain digits.")

    matched_records = []

    for record in book.addressbook.data.values():
        for phone_obj in record.phones:
            # Strip formatting from stored phone number to check raw digits
            stored_digits = Phone.get_num(phone_obj.value)
            if query_digits in stored_digits:
                matched_records.append(record)
                break  # Avoid adding the same contact twice if multiple phones match

    if not matched_records:
        return f"No contacts found matching phone number: '{args[0]}'"

    return format_contacts_table(matched_records)


@input_error
def contact_email_add(args, book: Book):
    try:
        name, email, *_ = args
    except ValueError:
        raise ValueError("Give me name and email please")

    record = book.addressbook.find(name)

    if record is None:
        record = Record(name)
        book.addressbook.add_record(record)

    record.add_email(email)
    return "Email added."


def contact_email_change(*args):
    return "Command 'contact_email_change' TO BE IMPLEMENTED"


def contact_email_delete(*args):
    return "Command 'contact_email_delete' TO BE IMPLEMENTED"


@input_error
def contact_email_search(args, book: Book) -> str:
    if not args:
        raise ValueError("Give me an email keyword to search for please")

    query = args[0].lower()
    matched_records = []

    for record in book.addressbook.data.values():
        for email_obj in record.emails:
            if query in email_obj.value.lower():
                matched_records.append(record)
                break

    if not matched_records:
        return f"No contacts found matching email: '{args[0]}'"

    return format_contacts_table(matched_records)


@input_error
def contact_birthday_set(args, book: Book) -> str:
    try:
        name, date_str, *_ = args
    except ValueError:
        raise ValueError("Give me name and birthday date please")

    if name not in book.addressbook.data:
        raise KeyError()  # Triggers contact not found error decoration

    record = book.addressbook.data[name]
    standard_birthday = normalize_date(date_str).strftime("%d.%m.%Y")
    record.set_birthday(standard_birthday)

    return f"Birthday set to {standard_birthday} for {name}."


@input_error
def contact_birthday_change(args, book: Book) -> str:
    # Setting and changing share identical mechanics under the hood
    try:
        name, new_date_str, *_ = args
    except ValueError:
        raise ValueError("Give me name and the new birthday date please")

    if name not in book.addressbook.data:
        raise KeyError()

    record = book.addressbook.data[name]
    standard_birthday = normalize_date(new_date_str).strftime("%d.%m.%Y")
    record.set_birthday(standard_birthday)

    return f"Birthday updated to {standard_birthday} for {name}."


@input_error
def contact_birthday_delete(args, book: Book) -> str:
    if not args:
        raise ValueError("Give me a contact name please")

    name = args[0]
    if name not in book.addressbook.data:
        raise KeyError()

    record = book.addressbook.data[name]
    if not getattr(record, "birthday", None):
        return f"{name} does not have a birthday set."

    record.birthday = None
    return f"Birthday removed for {name}."


@input_error
def contact_birthday_search(args, book: Book) -> str:
    if not args:
        raise ValueError("Give me a date or search term to look for please")

    search_input = args[0].strip()
    matched_records = []

    # Case A: User passes a fully qualified target date string to find matching contacts
    try:
        target_date = normalize_date(search_input)
        for record in book.addressbook.data.values():
            if (
                getattr(record, "birthday", None)
                and str(record.birthday) == target_date
            ):
                matched_records.append(record)

    # Case B: User passes a partial substring match scenario (e.g. searching just a month ".05." or year "1990")
    except ValueError:
        query = search_input.lower()
        for record in book.addressbook.data.values():
            if getattr(record, "birthday", None):
                if query in str(record.birthday).lower():
                    matched_records.append(record)

    if not matched_records:
        return f"No contacts found matching birthday: '{search_input}'"

    return format_contacts_table(matched_records)


@input_error
def show_all(args, book: Book) -> str:
    if not book.addressbook.data:
        return "No contacts."
    return format_contacts_table(list(book.addressbook.data.values()))


def contact_address_set(args, book: Book):
    try:
        name, *parts = args
    except ValueError:
        raise ValueError("Give me name and address please")

    record = book.addressbook.find(name)

    if record is None:
        record = Record(name)
        book.addressbook.add_record(record)

    record.set_address(" ".join(parts))
    return "Address updated."


def contact_address_change(*args):
    return "Command 'contact_ddress_change' TO BE IMPLEMENTED"


def contact_address_delete(*args):
    return "Command 'contact_address_delete' TO BE IMPLEMENTED"


@input_error
def contact_address_search(args, book: Book) -> str:
    if not args:
        raise ValueError("Give me an address keyword to search for please")

    query = " ".join(args).lower()
    matched_records = []

    for record in book.addressbook.data.values():
        if record.address and query in record.address.value.lower():
            matched_records.append(record)

    if not matched_records:
        return f"No contacts found matching address: '{' '.join(args)}'"

    return format_contacts_table(matched_records)
