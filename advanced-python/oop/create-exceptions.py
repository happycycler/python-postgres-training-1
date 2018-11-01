class MissingLabelError(KeyError):
    pass


class PageNotFoundError(LookupError):
    pass


class IncorrectPasswordError(ValueError):
    pass


class IncorrectUsernameError(ValueError):
    pass


class APIThrottleLimitError(RuntimeError):
    pass


def login():
    raise IncorrectPasswordError()


try:
    login()
except IncorrectUsernameError:
    print("Your username was incorrect.  Have you forgotten it?")
except IncorrectPasswordError:
    print("Your password was incorrect.  Have you forgotten it?")