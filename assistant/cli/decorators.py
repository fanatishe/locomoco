from functools import wraps
from assistant.utils.messages import good_bye


def input_error(func):
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
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            good_bye()

    return wrapper
