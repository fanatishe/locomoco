from assistant.contacts.record import Record


def format_contact(record: Record) -> str:
    """Single contact — key: value per line."""
    return "\n".join(f"{key}: {value}" for key, value in record.to_dict().items())


def format_contacts_table(records: list[Record]) -> str:
    """Multiple contacts — ASCII table."""
    rows = [record.to_dict() for record in records]
    headers = list(rows[0].keys())

    widths = {h: len(h) for h in headers}
    for row in rows:
        for h in headers:
            widths[h] = max(widths[h], len(row[h]))

    sep = "+" + "+".join("-" * (widths[h] + 2) for h in headers) + "+"
    header_row = "|" + "|".join(f" {h:<{widths[h]}} " for h in headers) + "|"

    lines = [sep, header_row, sep]
    for row in rows:
        lines.append("|" + "|".join(f" {row[h]:<{widths[h]}} " for h in headers) + "|")
    lines.append(sep)

    return "\n".join(lines)
