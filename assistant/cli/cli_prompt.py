from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.auto_suggest import AutoSuggest, Suggestion


commands_list = [
    "exit",
    "close",
    "hello",
    "contact",
    "contact add",
    "contact change",
    "contact delete",
    "contact search",
    "contact search name",
    "contact phone",
    "contact phone add",
    "contact phone change",
    "contact phone delete",
    "contact phone search",
    "contact email",
    "contact email add",
    "contact email change",
    "contact email delete",
    "contact email search",
    "contact birthday",
    "contact birthday set",
    "contact birthday change",
    "contact birthday delete",
    "contact birthday search",
    "contact address",
    "contact address set",
    "contact address change",
    "contact address delete",
    "contact address search",
    "note",
    "note add",
    "note change",
    "note delete",
    "note search",
    "note tag",
    "note tag add",
    "note tag change",
    "note tag delete",
    "note tag search",
    "help",
    "help contact",
    "help contact add",
    "help contact change",
    "help contact delete",
    "help contact search",
    "help contact phone",
    "help contact phone add",
    "help contact phone change",
    "help contact phone delete",
    "help contact phone search",
    "help contact email",
    "help contact email add",
    "help contact email change",
    "help contact email delete",
    "help contact email search",
    "help contact birthday",
    "help contact birthday set",
    "help contact birthday change",
    "help contact birthday delete",
    "help contact birthday search",
    "help contact address",
    "help contact address set",
    "help contact address change,",
    "help contact address delete",
    "help contact address search",
    "help note",
    "help note add",
    "help note change",
    "help note delete",
    "help note search",
    "help note tag",
    "help note tag add",
    "help note tag change",
    "help note tag delete",
    "help note tag search",
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
