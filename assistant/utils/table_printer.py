from rich.table import Table
from rich.console import Console
from io import StringIO

from assistant.contacts.record import Record
from assistant.utils.formatters import COLUMN_STYLES


def format_contact(record: Record) -> str:
    """Single contact — key: value per line."""
    return "\n".join(f"{key}: {value}" for key, value in record.to_dict().items())


def format_contacts_table(records: list[Record]) -> str:
    """Multiple contacts — styled table via rich library."""
    headers = list(records[0].to_dict().keys())

    table = Table(title="Contacts", show_lines=True)
    for h in headers:
        table.add_column(h, style=COLUMN_STYLES.get(h, ""))

    for record in records:
        table.add_row(*record.to_dict().values())

    # StringIO is an in-memory buffer that mimics a file.
    # Console writes to it instead of stdout, so we can capture the output as a string.
    # force_terminal=True tells rich to keep ANSI color codes even though it's not a real terminal.
    buffer = StringIO()
    Console(file=buffer, force_terminal=True).print(table)
    return buffer.getvalue()
