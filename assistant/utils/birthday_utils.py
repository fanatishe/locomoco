from datetime import date, datetime


def normalize_date(date_str: str) -> datetime:
    """
    Accepts DD.MM.YYYY or YYYY-MM-DD formats.
    Returns standard internal format DD.MM.YYYY.
    """
    date_str = date_str.strip()
    for fmt in ("%d.%m.%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError("Invalid date format. Please use DD.MM.YYYY or YYYY-MM-DD.")


def birthday_in_year(year: int, month: int, day: int) -> date:
    """
    Build a date for a given (year, month, day), shifting Feb 29 to Feb 28
    when the target year is not a leap year.

    Args:
        year (int): Target year.
        month (int): Birthday month.
        day (int): Birthday day.

    Returns:
        date: Concrete date in the requested year.
    """
    try:
        return date(year, month, day)
    except ValueError:
        # Only Feb 29 in a non-leap year reaches here.
        return date(year, month, day - 1)
