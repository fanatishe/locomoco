from assistant.utils.exceptions import ContactNotFoundError


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ContactNotFoundError as error:
            return str(error)

        except ValueError as error:
            return str(error)

        except IndexError:
            return "Enter command arguments."

    return inner
