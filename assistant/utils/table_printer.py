from rich.table import Table
from rich.console import Console
from io import StringIO

from assistant.contacts.record import Record
from assistant.utils.formatters import COLUMN_STYLES


def _render(table: Table) -> str:
    buffer = StringIO()
    Console(file=buffer, force_terminal=True).print(table)
    return buffer.getvalue()


def format_contact(record: Record) -> str:
    """Single contact — two-column rich table with field name and value."""
    table = Table(show_header=False, show_lines=True)
    table.add_column(style="bold")
    table.add_column()

    for key, value in record.to_dict().items():
        style = COLUMN_STYLES.get(key, "")
        table.add_row(key, value, style=style)

    return _render(table)


def format_contacts_table(records: list[Record]) -> str:
    """Multiple contacts — styled table via rich library."""
    headers = list(records[0].to_dict().keys())

    table = Table(title="Contacts", show_lines=True)
    for h in headers:
        table.add_column(h, style=COLUMN_STYLES.get(h, ""))

    for record in records:
        table.add_row(*record.to_dict().values())

    return _render(table)
