from functools import wraps


def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ...
    return wrapper


def unexpected_exit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except BaseException as e:
            print(e)
    return wrapper
