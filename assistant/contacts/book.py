from assistant.contacts.address_book import AddressBook
from assistant.contacts.notebook import Notebook


class Book:
    """
    The root application state object unifying both sub-stores (AddressBook and Notebook).
    This single object is what gets pickled and saved to the hard drive.
    """

    def __init__(self):
        self.addressbook = AddressBook()
        self.notebook = Notebook()
