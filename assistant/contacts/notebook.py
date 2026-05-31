from collections import UserDict


class Notebook(UserDict):
    """
    Holds standalone text notes separate from contacts, utilizing an auto-incrementing ID.
    """

    def __init__(self):
        super().__init__()
        self.current_id = 1

    def add_note(self, text: str) -> int:
        """
        Creates a new note with a unique integer ID.

        Args:
            text (str): The body text of the note.

        Returns:
            int: The unique identifier assigned to the note.
        """
        note_id = self.current_id
        self.data[note_id] = {"text": text, "tags": []}
        self.current_id += 1
        return note_id
