from assistant.contacts.address import Address
from assistant.contacts.email import Email
from assistant.contacts.name import Name
from assistant.contacts.phone import Phone

COLUMN_STYLES = {
    "Name": "bold cyan",
    "Phones": "green",
    "Address": "",
    "Emails": "yellow",
}


def format_name(name: Name) -> str:
    return str(name)


def format_phones(phones: list[Phone]) -> str:
    formatted_list = []
    for phone in phones:
        raw = str(phone.value)
        formatted = f"+38 ({raw[0:3]}) {raw[3:6]}-{raw[6:8]}-{raw[8:]}"
        formatted_list.append(formatted)

    return "\n".join(formatted_list) or "-"


def format_address(address: Address | None) -> str:
    return str(address) if address else "-"


def format_emails(emails: list[Email]) -> str:
    return "\n".join(str(email) for email in emails) or "-"
