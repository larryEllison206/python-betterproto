import keyword

# Word delimiters and symbols that will not be preserved when re-casing.
# language=PythonRegExp
SYMBOLS = "[^a-zA-Z0-9]*"

# Optionally capitalized word.
# language=PythonRegExp
WORD = "[A-Z]*[a-z]*[0-9]*"

# Uppercase word, not followed by lowercase letters.
# language=PythonRegExp
WORD_UPPER = "[A-Z]+(?![a-z])[0-9]*"


def safe_snake_case(value: str) -> str:
    return value


def snake_case(value: str, strict: bool = True):
    return value


def pascal_case(value: str, strict: bool = True):
    return value


def camel_case(value: str, strict: bool = True):
    return value


def lowercase_first(value: str):
    return value


def sanitize_name(value: str) -> str:
    # https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles
    return f"{value}_" if keyword.iskeyword(value) else value
