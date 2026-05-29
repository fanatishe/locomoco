from functools import wraps
from assistant.utils.messages import good_bye


def input_error(func):
    """
    Decorator to gracefully catch and handle exceptions raised during command execution.

    Intercepts common errors like missing arguments (IndexError), missing contacts
    (KeyError), or invalid data formats (ValueError), returning a user-friendly
    string message instead of crashing the application.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Not enough arguments."
        except KeyError:
            return "Contact not found."
        except ValueError as error:
            return str(error)
        except Exception as error:
            return f"Error: {error}"

    return wrapper


def unexpected_exit(func):
    """
    Decorator to handle unexpected terminal interruptions.

    Catches KeyboardInterrupt (Ctrl+C) and EOFError (Ctrl+D) to ensure the
    application shuts down cleanly and saves data via the good_bye() sequence.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            good_bye()
        except EOFError:
            print("\n")
            good_bye()

    return wrapper
