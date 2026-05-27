from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.auto_suggest import AutoSuggest, Suggestion


commands_list = [
    "contacts add",
    "contacts edit",
    "contacts delete",
    "contacts list",
    "contacts search",
    "contacts birthday",
    "contacts birthdays",
    "notes add",
    "notes edit",
    "notes delete",
    "notes tags",
    "help",
    "exit",
]


class AutoSuggestFromList(AutoSuggest):
    def __init__(self, words):
        self.words = words

    def get_suggestion(self, buffer, document):
        text = document.text
        if not text:
            return None

        # Look for a match in your static commands list
        for word in self.words:
            if word.startswith(text):
                # Return only the remaining trailing text
                return Suggestion(word[len(text) :])
        return None


kb = KeyBindings()


@kb.add("tab")
def _(event):
    """Pressing TAB accepts the current inline autosuggestion"""
    buffer = event.current_buffer
    suggestion = buffer.suggestion
    if suggestion:
        buffer.insert_text(suggestion.text)


history = InMemoryHistory()
session = PromptSession(
    history=history,
    auto_suggest=AutoSuggestFromList(commands_list),
    key_bindings=kb,
)


def get_user_input():
    while True:
        try:
            user_input = session.prompt("Enter a command: ")
        except Exception:
            user_input = input("Enter a command: ")

        return user_input
