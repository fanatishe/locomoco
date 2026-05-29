CYAN = "\033[96m"
RESET = "\033[0m"


def help_default(*args):
    return f"""
Welcome to the main help

Use {CYAN}exit{RESET} or {CYAN}close{RESET} to exit the assistant.
Usage: [command] [sub-command] [arguments]

Available Command Groups:
    {CYAN}contact{RESET} — Manage contact profiles (names, birthdays, addresses).
    {CYAN}note{RESET} — Create and manage text notes and tags.


Use {CYAN}help{RESET} {CYAN}<command>{RESET} to see a help for a specific command.
E.g. {CYAN}help contact{RESET}
"""


def help_contact(*args):
    return f"""
Command: {CYAN}contact{RESET}
Description: Manage contact profiles.

Available Actions:

    {CYAN}add{RESET} — Creates contact with specific name.
    {CYAN}change{RESET} — Update an existing contact's name.
    {CYAN}delete{RESET} — Remove a contact.
    {CYAN}search{RESET} — Find contact by name or all if not specified.
    
Available Sub-Groups:

    {CYAN}phone{RESET} — Manage phone numbers.
    {CYAN}email{RESET} — Manage email addresses.
    {CYAN}birthday{RESET} — Manage contact birthdays.
    {CYAN}address{RESET} — Manage contact physical addresses.
"""


def help_contact_add(*args):
    return f"""
Command: {CYAN}contact add{RESET}
Description: Create a new contact with a specific name.

Usage:
{CYAN}contact add <username> [phone_number] [birthday]{RESET}

Arguments:

    {CYAN}<username>{RESET} — The name of the new contact (wrap in quotes if it contains spaces).
    {CYAN}<phone_number>{RESET} (optional) — The phone number to add (digits only, e.g., 1234567890).
    {CYAN}<birthday>{RESET} (optional) — The birthday date (e.g., DD.MM.YYYY or YYYY-MM-DD).

Example:
contact add "John Doe"
"""


def help_contact_change(*args):
    return f"""
Command: {CYAN}contact change{RESET}
Description: Update an existing contact's name.

Usage:
{CYAN}contact change <old_username> <new_username>{RESET}

Arguments:

    {CYAN}<old_username>{RESET} — The current name of the contact.
    {CYAN}<new_username>{RESET} — The new name to assign to the contact.

Example:
contact change "John Doe" "Johnny Doe"
"""


def help_contact_delete(*args):
    return f"""
Command: {CYAN}contact delete{RESET}
Description: Remove a contact completely from the system.

Usage:
{CYAN}contact delete <username>{RESET}

Arguments:

    {CYAN}<username>{RESET} — The name of the contact to delete.

Example:
contact delete "John Doe"
"""


def help_contact_search(*args):
    return f"""
Command: {CYAN}contact search{RESET}
Description: Find a contact by name, or view all contacts if no name is specified.

Usage:
{CYAN}contact search [<username>]{RESET}

Arguments:

    {CYAN}<username>{RESET} — Optional. The name or part of the name to search for.

Example:
contact search John
"""


def help_contact_phone(*args):
    return f"""
Command: {CYAN}contact phone{RESET}
Description: Manage phone numbers associated with your contacts.

Available Actions:

    {CYAN}add{RESET} — Add a phone number to a contact (creates contact if it doesn't exist).
    {CYAN}change{RESET} — Update an existing contact's phone number.
    {CYAN}delete{RESET} — Remove a phone number from a contact.
    {CYAN}search{RESET} — Find contacts by phone number.
"""


def help_contact_phone_add(*args):
    return f"""
Command: {CYAN}contact phone add{RESET}
Description: Add a phone number to a contact. If the contact does not exist, a new one will be created.

Usage:
{CYAN}contact phone add <username> <phone_number>{RESET}

Arguments:

    {CYAN}<username>{RESET} — The name of the contact (wrap in quotes if it contains spaces).
    {CYAN}<phone_number>{RESET} — The phone number to add (digits only, e.g., 1234567890).

Example:
contact phone add "John Doe" +1234567890
"""


def help_contact_phone_change(*args):
    return f"""
Command: {CYAN}contact phone change{RESET}
Description: Update an existing phone number for a contact.

Usage:
{CYAN}contact phone change <username> <old_phone_number> <new_phone_number>{RESET}

Arguments:

    {CYAN}<username>{RESET} — The name of the contact.
    {CYAN}<old_phone_number>{RESET} — The number you want to change.
    {CYAN}<new_phone_number>{RESET} — The new phone number to save.

Example:
contact phone change "John Doe" +1234567890 +1987654321
"""


def help_contact_phone_delete(*args):
    return f"""
Command: {CYAN}contact phone delete{RESET}
Description: Remove a specific phone number from a contact.

Usage:
{CYAN}contact phone delete <username> <phone_number>{RESET}

Arguments:

    {CYAN}<username>{RESET} — The name of the contact.
    {CYAN}<phone_number>{RESET} — The phone number to remove.

Example:
contact phone delete "John Doe" +1234567890
"""


def help_contact_phone_search(*args):
    return f"""
Command: {CYAN}contact phone search{RESET}
Description: Find contacts matching a specific phone number.

Usage:
{CYAN}contact phone search <phone_number>{RESET}

Arguments:

    {CYAN}<phone_number>{RESET} — The phone number or part of the phone number to search for.

Example:
contact phone search 555-0199
"""


def help_contact_email(*args):
    return f"""
Command: {CYAN}contact email{RESET}
Description: Manage email addresses associated with your contacts.

Available Actions:

    {CYAN}add{RESET} — Add an email address to a contact (creates contact if it doesn't exist).
    {CYAN}change{RESET} — Update an existing contact's email address.
    {CYAN}delete{RESET} — Remove an email address from a contact.
    {CYAN}search{RESET} — Find contacts by email address.
"""


def help_contact_email_add(*args):
    return f"""
Command: {CYAN}contact email add{RESET}
Description: Add an email address to a contact. If the contact does not exist, a new one will be created.

Usage:
{CYAN}contact email add <username> <email>{RESET}

Arguments:

    {CYAN}<username>{RESET} — The name of the contact.
    {CYAN}<email>{RESET} — The email address to add (e.g., example@domain.com).

Example:
contact email add "John Doe" john@example.com
"""


def help_contact_email_change(*args):
    return f"""
Command: {CYAN}contact email change{RESET}
Description: Update an existing email address for a contact.

Usage:
{CYAN}contact email change <username> <old_email> <new_email>{RESET}

Arguments:

    {CYAN}<username>{RESET} — The name of the contact.
    {CYAN}<old_email>{RESET} — The email address you want to change.
    {CYAN}<new_email>{RESET} — The new email address to save.

Example:
contact email change "John Doe" old@example.com new@example.com
"""


def help_contact_email_delete(*args):
    return f"""
Command: {CYAN}contact email delete{RESET}
Description: Remove a specific email address from a contact.

Usage:
{CYAN}contact email delete <username> <email>{RESET}

Arguments:

    {CYAN}<username>{RESET} — The name of the contact.
    {CYAN}<email>{RESET} — The email address to remove.

Example:
contact email delete "John Doe" john@example.com
"""


def help_contact_email_search(*args):
    return f"""
Command: {CYAN}contact email search{RESET}
Description: Find contacts matching a specific email address.

Usage:
{CYAN}contact email search <email>{RESET}

Arguments:

    {CYAN}<email>{RESET} — The email address or part of the address to search for.

Example:
contact email search john@example.com
"""


def help_contact_birthday(*args):
    return f"""
Command: {CYAN}contact birthday{RESET}
Description: Manage birthdays associated with your contacts.

Available Actions:

    {CYAN}set{RESET} — Set a birthday for a contact (creates contact if it doesn't exist).
    {CYAN}change{RESET} — Update an existing contact's birthday.
    {CYAN}delete{RESET} — Remove a birthday from a contact.
    {CYAN}search{RESET} — Find contacts by birthday or see upcoming birthdays.
"""


def help_contact_birthday_set(*args):
    return f"""
Command: {CYAN}contact birthday set{RESET}
Description: Set a birthday for a contact. If the contact does not exist, a new one will be created.

Usage:
{CYAN}contact birthday set <username> <date>{RESET}

Arguments:

    {CYAN}<username>{RESET} — The name of the contact.
    {CYAN}<date>{RESET} — The birthday date (e.g., DD.MM.YYYY or YYYY-MM-DD).

Example:
contact birthday set "John Doe" 15.05.1990
"""


def help_contact_birthday_change(*args):
    return f"""
Command: {CYAN}contact birthday change{RESET}
Description: Change the birthday date for an existing contact.

Usage:
{CYAN}contact birthday change <username> <new_date>{RESET}

Arguments:

    {CYAN}<username>{RESET} — The name of the contact.
    {CYAN}<new_date>{RESET} — The new birthday date (e.g., DD.MM.YYYY or YYYY-MM-DD).

Example:
contact birthday change "John Doe" 20.05.1990
"""


def help_contact_birthday_delete(*args):
    return f"""
Command: {CYAN}contact birthday delete{RESET}
Description: Remove the birthday data from a contact.

Usage:
{CYAN}contact birthday delete <username>{RESET}

Arguments:

    {CYAN}<username>{RESET} — The name of the contact.

Example:
contact birthday delete "John Doe"
"""


def help_contact_birthday_search(*args):
    return f"""
Command: {CYAN}contact birthday search{RESET}
Description: Find contacts by birthday or view upcoming birthdays.

Usage:
{CYAN}contact birthday search <date_or_days>{RESET}

Arguments:

    {CYAN}<date_or_days>{RESET} — A specific date to look up, or a number of days to check for upcoming birthdays.

Example:
contact birthday search 7
"""


def help_contact_address(*args):
    return f"""
Command: {CYAN}contact address{RESET}
Description: Manage physical addresses associated with your contacts.

Available Actions:

    {CYAN}set{RESET} — Set an address for a contact (creates contact if it doesn't exist).
    {CYAN}change{RESET} — Update an existing contact's address.
    {CYAN}delete{RESET} — Remove an address from a contact.
    {CYAN}search{RESET} — Find contacts by address.
"""


def help_contact_address_set(*args):
    return f"""
Command: {CYAN}contact address set{RESET}
Description: Set a physical address for a contact. If the contact does not exist, a new one will be created.

Usage:
{CYAN}contact address set <username> <address>{RESET}

Arguments:

    {CYAN}<username>{RESET} — The name of the contact.
    {CYAN}<address>{RESET} — The full physical address (wrap in quotes).

Example:
contact address set "John Doe" "123 Main St, New York, NY"
"""


def help_contact_address_change(*args):
    return f"""
Command: {CYAN}contact address change{RESET}
Description: Update the physical address for an existing contact.

Usage:
{CYAN}contact address change <username> <new_address>{RESET}

Arguments:

    {CYAN}<username>{RESET} — The name of the contact.
    {CYAN}<new_address>{RESET} — The new address text (wrap in quotes).

Example:
contact address change "John Doe" "456 Oak Ave, Boston, MA"
"""


def help_contact_address_delete(*args):
    return f"""
Command: {CYAN}contact address delete{RESET}
Description: Remove the physical address from a contact.

Usage:
{CYAN}contact address delete <username>{RESET}

Arguments:

    {CYAN}<username>{RESET} — The name of the contact.

Example:
contact address delete "John Doe"
"""


def help_contact_address_search(*args):
    return f"""
Command: {CYAN}contact address search{RESET}
Description: Find contacts matching a specific address text.

Usage:
{CYAN}contact address search <address>{RESET}

Arguments:

    {CYAN}<address>{RESET} — The address string or city/street keywords to look up.

Example:
contact address search "New York"
"""


def help_note(*args):
    return f"""
Command: {CYAN}note{RESET}
Description: Create and manage text notes.

Available Actions:

    {CYAN}add{RESET} — Create a new note.
    {CYAN}change{RESET} — Update the content of an existing note.
    {CYAN}delete{RESET} — Remove a specific note.
    {CYAN}search{RESET} — Find notes by keyword or content.

Available Sub-Groups:

    {CYAN}tag{RESET} — Manage categories and tags attached to notes.
"""


def help_note_add(*args):
    return f"""
Command: {CYAN}note add{RESET}
Description: Create a new text note.

Usage:
{CYAN}note add <title> <content>{RESET}

Arguments:

    {CYAN}<title>{RESET} — The title or identifier of the note (wrap in quotes if multiple words).
    {CYAN}<content>{RESET} — The body text of the note.

Example:
note add "Shopping List" "Buy milk, eggs, and bread"
"""


def help_note_delete(*args):
    return f"""
Command: {CYAN}note delete{RESET}
Description: Delete a specific note.

Usage:
{CYAN}note delete <title>{RESET}

Arguments:

    {CYAN}<title>{RESET} — The title of the note you wish to delete.

Example:
note delete "Shopping List"
"""


def help_note_search(*args):
    return f"""
Command: {CYAN}note search{RESET}
Description: Search through notes by titles or keywords within contents.

Usage:
{CYAN}note search <keyword>{RESET}

Arguments:

    {CYAN}<keyword>{RESET} — The keyword or phrase to search for.

Example:
note search milk
"""


def help_note_tag(*args):
    return f"""
Command: {CYAN}note tag{RESET}
Description: Manage tags associated with your notes.

Available Actions:
    {CYAN}add{RESET} — Assign a tag to a note.
    {CYAN}change{RESET} — Replace an old tag with a new one on a specific note.
    {CYAN}delete{RESET} — Remove a tag from a note.
    {CYAN}search{RESET} — Filter and find notes matching specific tags.
    {CYAN}sort{RESET} — Sort all notes alphabetically by their tags.
"""


def help_note_tag_add(*args):
    return f"""
Command: {CYAN}note tag add{RESET}
Description: Add a tag to a specific note to categorize it.

Usage:
{CYAN}note tag add <title> <tag_name>{RESET}

Arguments:

    {CYAN}<title>{RESET} — The title of the note.
    {CYAN}<tag_name>{RESET} — The tag to attach (e.g., todo, work).

Example:
note tag add "Shopping List" grocery
"""


def help_note_tag_change(*args):
    return f"""
Command: {CYAN}note tag change{RESET}
Description: Replace an existing tag with a new tag name on a specific note.

Usage:
{CYAN}note tag change <title> <old_tag_name> <new_tag_name>{RESET}

Arguments:

    {CYAN}<title>{RESET} — The title of the note.
    {CYAN}<old_tag_name>{RESET} — The existing tag you want to update.
    {CYAN}<new_tag_name>{RESET} — The new tag name to replace it with.

Example:
note tag change "Shopping List" grocery food
"""


def help_note_tag_search(*args):
    return f"""
Command: {CYAN}note tag search{RESET}
Description: Find all notes that match a specific tag.

Usage:
{CYAN}note tag search <tag_name>{RESET}

Arguments:

    {CYAN}<tag_name>{RESET} — The tag name to filter notes by.

Example:
note tag search todo
"""


def help_note_change(*args):
    return f"""
Command: {CYAN}note change{RESET}
Description: Update or overwrite the text content of an existing note.

Usage:
{CYAN}note change <title> <new_content>{RESET}

Arguments:

    {CYAN}<title>{RESET} — The title of the note you want to update.
    {CYAN}<new_content>{RESET} — The new text body that will replace the old content.

Example:
note change "Shopping List" "Buy milk, eggs, bread, and coffee"
"""


def help_note_tag_delete(*args):
    return f"""
Command: {CYAN}note tag delete{RESET}
Description: Remove a specific tag from a note.

Usage:
{CYAN}note tag delete <title> <tag_name>{RESET}

Arguments:

    {CYAN}<title>{RESET} — The title of the note.
    {CYAN}<tag_name>{RESET} — The tag to remove.

Example:
note tag delete "Shopping List" grocery
"""


def help_note_tag_sort(*args):
    return f"""
Command: {CYAN}note tag sort{RESET}
Description: Displays all notes sorted alphabetically by their tags. Notes without tags are shown at the bottom.

Usage:
{CYAN}note tag sort{RESET}

Example:
note tag sort
"""
