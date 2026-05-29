from ..contacts.address_book import AddressBook
from ..contacts.record import Record


def run_tests():
    mock = [
        {
            "name": "John",
            "phone": "0971232132",
            "bd": "29.05.1990"
        },
        {
            "name": "Mary",
            "phone": "0634901287",
            "bd": "06.06.1990"
        },
        {
            "name": "Ken",
            "phone": "0670125476",
            "bd": "16.06.1990"
        },
        {
            "name": "Pete",
            "phone": "0670125476"
        }
    ]
    book = AddressBook()

    for i in mock:
        r = Record(i["name"])
        r.add_phone(i["phone"])
        bd = i.get("bd")
        if bd:
            r.add_birthday(bd)
        book.add_record(r)

    print("\n=== show contacts from today within 7 ===")
    book.show_upcoming_birthdays()

    print("\n=== show contacts from 1.06.2026 within 16 ===")
    book.show_upcoming_birthdays(from_date="1.06.2026", within=16)

if __name__ == "__main__":
    run_tests()