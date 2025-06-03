import sys

class FileError(Exception):
    pass

class MissingBreaker(Exception):
    pass

class InvalidNode(Exception):
    pass

class LexerError(Exception):
    pass

class ASTJSONCreateError(Exception):
    pass

class RangeException(Exception):
    pass

def clean_exit_hook(exc_type, exc_value, _):
    if exc_type.__name__ in ["InvalidNode", "MissingBreaker", "RangeException"]:
        print(f"\033[1;35m{exc_type.__name__}:\033[0;35m {exc_value}\033[0m")
    else:
        sys.__excepthook__(exc_type, exc_value, _)

sys.excepthook = clean_exit_hook