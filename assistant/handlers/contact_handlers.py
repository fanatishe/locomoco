from assistant.contacts.record import Record
from assistant.cli.decorators import input_error
from assistant.utils.table_printer import format_contacts_table
from assistant.contacts.address_book import Book
from assistant.contacts.phone import Phone
from assistant.contacts.email import Email
from assistant.contacts.name import Name
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


@input_error
def contact_change(args, book: Book):
    try:
        old_name, new_name, *_ = args
    except ValueError:
        raise ValueError("Give me the old name and the new name please")

    if old_name not in book.addressbook.data:
        raise KeyError()

    if new_name in book.addressbook.data:
        raise ValueError(f"Contact with the name '{new_name}' already exists.")

    record = book.addressbook.data[old_name]
    record.name = Name(new_name)
    book.addressbook.data[new_name] = record
    del book.addressbook.data[old_name]

    return f"Contact name updated from '{old_name}' to '{new_name}'."


@input_error
def contact_delete(args, book: Book):
    if not args:
        raise ValueError("Give me a contact name to delete please")

    name = args[0]
    if name not in book.addressbook.data:
        raise KeyError()

    del book.addressbook.data[name]
    return f"Contact '{name}' removed completely from the system."


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


@input_error
def contact_phone_add(args, book: Book):
    try:
        name, phone, *_ = args
    except ValueError:
        raise ValueError("Give me name and phone number please")

    record = book.addressbook.find(name)

    if record is None:
        record = Record(name)
        book.addressbook.add_record(record)

    record.add_phone(phone)
    return f"Phone number '{phone}' added to contact {name}."


@input_error
def contact_phone_change(args, book: Book):
    try:
        name, old_phone, new_phone, *_ = args
    except ValueError:
        raise ValueError("Give me name, old phone, and new phone number please")

    if name not in book.addressbook.data:
        raise KeyError()

    record = book.addressbook.data[name]
    target_digits = Phone.get_num(old_phone)

    for idx, phone_obj in enumerate(record.phones):
        if Phone.get_num(phone_obj.value) == target_digits:
            record.phones[idx] = Phone(new_phone)
            return (
                f"Phone number updated from '{old_phone}' to '{new_phone}' for {name}."
            )

    return f"Phone number '{old_phone}' not found for contact {name}."


@input_error
def contact_phone_delete(args, book: Book):
    try:
        name, phone, *_ = args
    except ValueError:
        raise ValueError("Give me name and phone number to delete please")

    if name not in book.addressbook.data:
        raise KeyError()

    record = book.addressbook.data[name]
    target_digits = Phone.get_num(phone)

    for phone_obj in record.phones:
        if Phone.get_num(phone_obj.value) == target_digits:
            record.phones.remove(phone_obj)
            return f"Phone number '{phone}' removed from contact {name}."

    return f"Phone number '{phone}' not found for contact {name}."


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


@input_error
def contact_email_change(args, book: Book):
    try:
        name, old_email, new_email, *_ = args
    except ValueError:
        raise ValueError("Give me name, old email, and new email please")

    if name not in book.addressbook.data:
        raise KeyError()

    record = book.addressbook.data[name]
    old_email_clean = old_email.strip().lower()

    for idx, email_obj in enumerate(record.emails):
        if email_obj.value.lower() == old_email_clean:
            record.emails[idx] = Email(new_email)
            return f"Email updated from '{old_email}' to '{new_email}' for {name}."

    return f"Email '{old_email}' not found for contact {name}."


@input_error
def contact_email_delete(args, book: Book):
    try:
        name, email, *_ = args
    except ValueError:
        raise ValueError("Give me name and email to delete please")

    if name not in book.addressbook.data:
        raise KeyError()

    record = book.addressbook.data[name]
    email_clean = email.strip().lower()

    for email_obj in record.emails:
        if email_obj.value.lower() == email_clean:
            record.emails.remove(email_obj)
            return f"Email '{email}' removed from contact {name}."

    return f"Email '{email}' not found for contact {name}."


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
    """
    Searches for contacts by a specific birthday or checks for upcoming birthdays
    if a number of days is provided.

    Args:
        args (list[str]): User input. Can be a date string ("15.05") or an integer ("7").
        book (Book): The root application state.

    Returns:
        str: Formatted table of matching contacts.
    """
    if not args:
        raise ValueError("Give me a date or number of days to look for please")

    search_input = args[0].strip()

    # Case 1: The user passed an integer to find upcoming birthdays (tz.txt requirement)
    if search_input.isdigit():
        days = int(search_input)
        matched_records = book.addressbook.get_upcoming_birthdays(days)
        if not matched_records:
            return f"No upcoming birthdays in the next {days} days."
        return format_contacts_table(matched_records)

    # Case 2: User passed a date substring (e.g., a specific year "1990" or month ".05.")
    matched_records = []
    query = search_input.lower()

    for record in book.addressbook.data.values():
        if getattr(record, "birthday", None):
            if query in str(record.birthday).lower():
                matched_records.append(record)

    if not matched_records:
        return f"No contacts found matching birthday query: '{search_input}'"

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


@input_error
def contact_address_change(args, book: Book):
    try:
        name, *address_parts = args
    except ValueError:
        raise ValueError("Give me name and new address details please")

    if not address_parts:
        raise ValueError("Give me name and new address details please")

    if name not in book.addressbook.data:
        raise KeyError()

    new_address = " ".join(address_parts)
    record = book.addressbook.data[name]
    record.set_address(new_address)
    return f"Address updated for {name}."


@input_error
def contact_address_delete(args, book: Book):
    if not args:
        raise ValueError("Give me a contact name please")

    name = args[0]
    if name not in book.addressbook.data:
        raise KeyError()

    record = book.addressbook.data[name]
    if not record.address:
        return f"{name} does not have a saved physical address."

    record.address = None
    return f"Address removed for {name}."


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
