import sys
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.auto_suggest import AutoSuggest, Suggestion
from assistant.cli.commands import commands_list as commands_list_handlers

commands_list = commands_list_handlers.keys()


class AutoSuggestFromList(AutoSuggest):
    """
    Provides inline auto-suggestions in the terminal based on a static list of commands.
    """

    def __init__(self, words: list[str]):
        """
        Initializes the auto-suggester with the available application commands.

        Args:
            words (list[str]): A list of valid command strings.
        """
        self.words = words

    def get_suggestion(self, buffer, document) -> Suggestion | None:
        """
        Evaluates the current user input buffer and returns the remaining text of a matching command.
        """
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


# Set session to None initially to avoid the fd=0 warning
session = None


def get_user_input() -> str:
    """
    Captures user input based on the current execution environment.

    If running interactively, initializes the prompt_toolkit session to provide
    auto-completion and history. If running via pipe/redirection (for E2E tests),
    bypasses the interactive UI and uses standard input().

    Returns:
        str: The raw string command entered by the user.
    """
    global session

    # 1. If we are piping/redirecting, bypass prompt_toolkit completely
    if not sys.stdin.isatty():
        return input()

    # 2. Only initialize the PromptSession if we are in an interactive terminal
    if session is None:
        history = InMemoryHistory()
        session = PromptSession(
            history=history,
            auto_suggest=AutoSuggestFromList(list(commands_list)),
            key_bindings=kb,
        )

    # 3. Proceed with the interactive prompt
    while True:
        try:
            user_input = session.prompt("Enter a command: ")
        except Exception:
            user_input = input("Enter a command: ")

        return user_input
