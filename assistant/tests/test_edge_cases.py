import sys
import os

# Force Python to find the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from assistant.contacts.record import Record
from assistant.contacts.phone import Phone
from assistant.utils.birthday_utils import normalize_date


def test_edge_cases():
    print("\n=== Edge Cases & Validation ===")

    # 1. Phone number formatting & scrubbing
    print("\n--- Phone Character Scrubbing ---")
    p1 = Phone("+38(050)123-45-67")
    print(f"Input: '+38(050)123-45-67' -> Stored as: {p1.value}")

    # 2. Duplicate phone validation
    print("\n--- Duplicate Phone Rejection ---")
    rec = Record("Alice")
    rec.add_phone("0501234567")
    try:
        rec.add_phone("0501234567")
        print("[!] BUG: Allowed duplicate phone number!")
    except ValueError as e:
        print(f"Success! Caught expected error: {e}")

    # 3. Invalid Date Validation (e.g., February 30th or wrong formats)
    print("\n--- Invalid Dates Rejection ---")
    bad_dates = ["30.02.2020", "2020/05/15", "yesterday"]
    for d in bad_dates:
        try:
            normalize_date(d)
            print(f"[!] BUG: Allowed invalid date: {d}")
        except ValueError as e:
            print(f"Input '{d}' -> Caught: {e}")


if __name__ == "__main__":
    test_edge_cases()
