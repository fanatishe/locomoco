def input_error(func):
    def inner(*args, **kwargs):
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

    return inner
