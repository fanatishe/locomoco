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


def format_notes_table(notes: list[dict]) -> str:
    """
    Takes a list of note dictionaries and formats them into a styled rich table.
    Expected dict format: {"id": int, "tags": list[str], "text": str}
    """
    if not notes:
        return "No notes found."

    table = Table(title="Notebook", show_lines=True)

    # Define columns with custom styles and justification
    table.add_column("ID", style="cyan", justify="center", width=4)
    table.add_column("Tags", style="yellow")
    table.add_column("Note Text", style="white")

    for note in notes:
        # Safely extract and format the data
        note_id = str(note.get("id", ""))
        tags_list = note.get("tags", [])
        tags_str = ", ".join(tags_list) if tags_list else "-"
        text_str = note.get("text", "")

        table.add_row(note_id, tags_str, text_str)

    return _render(table)
