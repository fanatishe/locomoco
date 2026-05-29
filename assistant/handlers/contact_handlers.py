from assistant.contacts.record import Record
from assistant.cli.decorators import input_error
from assistant.utils.table_printer import format_contacts_table
from assistant.contacts.address_book import Book
from assistant.contacts.phone import Phone
from assistant.contacts.email import Email
from assistant.contacts.name import Name
from assistant.utils.birthday_utils import normalize_date


@input_error
def contact_add(args: list[str], book: Book) -> str:
    """
    Creates a new contact profile. Optionally accepts a phone number and birthday.

    Args:
        args (list[str]): User input containing the name, and optionally phone and birthday.
        book (Book): The root application state containing the address book.

    Returns:
        str: A success message indicating the contact was added.

    Raises:
        ValueError: If the required name argument is missing.
    """
    try:
        name, *extra_args = args
    except ValueError:
        raise ValueError("Give me name please")

    # Retrieve existing contact or create a new one
    if name in book.addressbook.data:
        record = book.addressbook.data[name]
    else:
        record = Record(name)
        book.addressbook.add_record(record)

    # Handle the optional phone number
    if len(args) > 1:
        phone = args[1]
        record.add_phone(phone)

    # Handle the optional birthday
    if len(args) > 2:
        birthday_str = args[2]
        standard_birthday = normalize_date(birthday_str).strftime("%d.%m.%Y")
        record.set_birthday(standard_birthday)

    return "Contact added."


@input_error
def contact_change(args: list[str], book: Book) -> str:
    """
    Updates the primary name of an existing contact.

    Args:
        args (list[str]): User input containing the old name and the new name.
        book (Book): The root application state.

    Returns:
        str: A success message indicating the name was changed.

    Raises:
        ValueError: If the arguments are missing or if the new name already exists.
        KeyError: If the original contact name is not found.
    """
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
def contact_delete(args: list[str], book: Book) -> str:
    """
    Permanently removes a contact and all associated data from the address book.

    Args:
        args (list[str]): User input containing the name of the contact to delete.
        book (Book): The root application state.

    Returns:
        str: A success message confirming deletion.

    Raises:
        ValueError: If the contact name argument is missing.
        KeyError: If the contact is not found in the address book.
    """
    if not args:
        raise ValueError("Give me a contact name to delete please")

    name = args[0]
    if name not in book.addressbook.data:
        raise KeyError()

    del book.addressbook.data[name]
    return f"Contact '{name}' removed completely from the system."


@input_error
def contact_search(args: list[str], book: Book) -> str:
    """
    Searches for contacts matching a query across names, phones, emails, addresses, and birthdays.
    If no query is provided, it returns a formatted table of all contacts.

    Args:
        args (list[str]): An optional list containing a single search string.
        book (Book): The root application state.

    Returns:
        str: A visually formatted rich table of matching contacts, or an empty state message.
    """
    # If no arguments are passed, show all contacts
    if not args or not args[0].strip():
        if not book.addressbook.data:
            return "No contacts found."
        return format_contacts_table(list(book.addressbook.data.values()))

    query = args[0].lower()
    matched_records = []

    for name, record in book.addressbook.data.items():
        # Check Name
        if query in name.lower():
            matched_records.append(record)
            continue

        # Check Phones
        if any(query in phone.value for phone in record.phones):
            matched_records.append(record)
            continue

        # Check Emails
        if any(query in email.value.lower() for email in record.emails):
            matched_records.append(record)
            continue

        # Check Address
        if record.address and query in record.address.value.lower():
            matched_records.append(record)
            continue

        # Check Birthday
        if record.birthday and query in str(record.birthday.value).lower():
            matched_records.append(record)
            continue

    if not matched_records:
        return f"No contacts found matching query: '{args[0]}'"

    return format_contacts_table(matched_records)


@input_error
def contact_phone_add(args: list[str], book: Book) -> str:
    """
    Adds a new phone number to a contact. Creates the contact if it doesn't exist.

    Args:
        args (list[str]): User input containing the contact name and phone number.
        book (Book): The root application state.

    Returns:
        str: A success message indicating the phone number was added.
    """
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
def contact_phone_change(args: list[str], book: Book) -> str:
    """
    Updates an existing phone number for a specific contact.

    Args:
        args (list[str]): User input containing name, old phone number, and new phone number.
        book (Book): The root application state.

    Returns:
        str: A success message indicating the phone number was updated.
    """
    try:
        name, old_phone, new_phone, *_ = args
    except ValueError:
        raise ValueError("Give me name, old phone, and new phone number please")

    if name not in book.addressbook.data:
        raise KeyError()

    record = book.addressbook.data[name]
    target_digits = Phone.get_num(old_phone)
    new_digits = Phone.get_num(new_phone)

    if any(Phone.get_num(p.value) == new_digits for p in record.phones):
        raise ValueError(f"Phone number '{new_phone}' already exists for {name}.")

    for idx, phone_obj in enumerate(record.phones):
        if Phone.get_num(phone_obj.value) == target_digits:
            record.phones[idx] = Phone(new_phone)
            return (
                f"Phone number updated from '{old_phone}' to '{new_phone}' for {name}."
            )

    return f"Phone number '{old_phone}' not found for contact {name}."


@input_error
def contact_phone_delete(args: list[str], book: Book) -> str:
    """
    Removes a specific phone number from a contact.

    Args:
        args (list[str]): User input containing the contact name and the phone number to delete.
        book (Book): The root application state.

    Returns:
        str: A success message confirming deletion.
    """
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
def contact_phone_search(args: list[str], book: Book) -> str:
    """
    Searches for contacts matching a specific phone number.

    Args:
        args (list[str]): User input containing the phone number digits to search for.
        book (Book): The root application state.

    Returns:
        str: A formatted table of matching contacts.
    """
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
def contact_email_add(args: list[str], book: Book) -> str:
    """
    Adds a new email address to a contact. Creates the contact if it doesn't exist.

    Args:
        args (list[str]): User input containing the contact name and email address.
        book (Book): The root application state.

    Returns:
        str: A success message indicating the email was added.
    """
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
def contact_email_change(args: list[str], book: Book) -> str:
    """
    Updates an existing email address for a specific contact.

    Args:
        args (list[str]): User input containing name, old email, and new email.
        book (Book): The root application state.

    Returns:
        str: A success message indicating the email was updated.
    """
    try:
        name, old_email, new_email, *_ = args
    except ValueError:
        raise ValueError("Give me name, old email, and new email please")

    if name not in book.addressbook.data:
        raise KeyError()

    record = book.addressbook.data[name]
    old_email_clean = old_email.strip().lower()
    new_email_clean = new_email.strip().lower()

    if any(e.value.lower() == new_email_clean for e in record.emails):
        raise ValueError(f"Email '{new_email}' already exists for {name}.")

    for idx, email_obj in enumerate(record.emails):
        if email_obj.value.lower() == old_email_clean:
            record.emails[idx] = Email(new_email)
            return f"Email updated from '{old_email}' to '{new_email}' for {name}."

    return f"Email '{old_email}' not found for contact {name}."


@input_error
def contact_email_delete(args: list[str], book: Book) -> str:
    """
    Removes a specific email address from a contact.

    Args:
        args (list[str]): User input containing the contact name and email to delete.
        book (Book): The root application state.

    Returns:
        str: A success message confirming deletion.
    """
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
def contact_email_search(args: list[str], book: Book) -> str:
    """
    Searches for contacts matching a specific email keyword.

    Args:
        args (list[str]): User input containing the email string to search for.
        book (Book): The root application state.

    Returns:
        str: A formatted table of matching contacts.
    """
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
def contact_birthday_set(args: list[str], book: Book) -> str:
    """
    Sets the birthday date for a specific contact.

    Args:
        args (list[str]): User input containing the contact name and birthday date.
        book (Book): The root application state.

    Returns:
        str: A success message confirming the birthday was set.
    """
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
def contact_birthday_change(args: list[str], book: Book) -> str:
    """
    Updates the existing birthday date for a specific contact.

    Args:
        args (list[str]): User input containing the contact name and new birthday date.
        book (Book): The root application state.

    Returns:
        str: A success message confirming the birthday was updated.
    """
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
def contact_birthday_delete(args: list[str], book: Book) -> str:
    """
    Removes the birthday data from a specific contact.

    Args:
        args (list[str]): User input containing the contact name.
        book (Book): The root application state.

    Returns:
        str: A success message confirming the birthday was removed.
    """
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
def show_all(args: list[str], book: Book) -> str:
    """
    Retrieves and displays all contacts in the address book.

    Args:
        args (list[str]): Ignored arguments.
        book (Book): The root application state.

    Returns:
        str: A formatted table containing all saved contacts.
    """
    if not book.addressbook.data:
        return "No contacts."
    return format_contacts_table(list(book.addressbook.data.values()))


@input_error
def contact_address_set(args: list[str], book: Book) -> str:
    """
    Sets the physical address for a specific contact.

    Args:
        args (list[str]): User input containing the contact name and address string.
        book (Book): The root application state.

    Returns:
        str: A success message confirming the address was updated.
    """
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
def contact_address_change(args: list[str], book: Book) -> str:
    """
    Updates the physical address for a specific contact.

    Args:
        args (list[str]): User input containing the contact name and the new address string.
        book (Book): The root application state.

    Returns:
        str: A success message confirming the address was updated.
    """
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
def contact_address_delete(args: list[str], book: Book) -> str:
    """
    Removes the physical address data from a specific contact.

    Args:
        args (list[str]): User input containing the contact name.
        book (Book): The root application state.

    Returns:
        str: A success message confirming the address was removed.
    """
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
def contact_address_search(args: list[str], book: Book) -> str:
    """
    Searches for contacts matching a specific physical address keyword.

    Args:
        args (list[str]): User input containing the address string to search for.
        book (Book): The root application state.

    Returns:
        str: A formatted table of matching contacts.
    """
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
