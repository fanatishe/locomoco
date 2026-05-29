import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from assistant.contacts.address_book import AddressBook
from assistant.contacts.record import Record


def run_tests():
    mock = [
        {"name": "John", "phone": "0971232132", "bd": "29.05.1990"},
        {"name": "Mary", "phone": "0634901287", "bd": "06.06.1990"},
        {"name": "Ken", "phone": "0670125476", "bd": "16.06.1990"},
        {"name": "Pete", "phone": "0670125476"},
    ]
    book = AddressBook()

    for i in mock:
        r = Record(i["name"])
        r.add_phone(i["phone"])
        bd = i.get("bd")
        if bd:
            r.set_birthday(bd)  # FIXED: was add_birthday
        book.add_record(r)

    print("\n=== show contacts from today within 7 ===")
    # FIXED: call the correct method and print the result
    upcoming_7 = book.get_upcoming_birthdays(7)
    for record in upcoming_7:
        print(record)

    print("\n=== show contacts from today within 16 ===")
    # FIXED: removed invalid 'from_date' argument
    upcoming_16 = book.get_upcoming_birthdays(16)
    for record in upcoming_16:
        print(record)


if __name__ == "__main__":
    run_tests()
