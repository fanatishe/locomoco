class Field:
    """Represents a contact's generic field"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
