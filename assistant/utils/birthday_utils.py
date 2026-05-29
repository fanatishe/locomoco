from datetime import datetime


def normalize_date(date_str: str) -> str:
    """
    Accepts DD.MM.YYYY or YYYY-MM-DD formats.
    Returns standard internal format DD.MM.YYYY.
    """
    date_str = date_str.strip()
    for fmt in ("%d.%m.%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(date_str, fmt).strftime("%d.%m.%Y")
        except ValueError:
            continue
    raise ValueError("Invalid date format. Please use DD.MM.YYYY or YYYY-MM-DD.")
