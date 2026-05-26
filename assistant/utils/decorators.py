def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ValueError as error:
            return str(error)

        except IndexError:
            return "Enter command arguments."

    return inner
