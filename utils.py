import os

from constants import _get_digits


def string_to_int(list_of_strings: list[str]) -> list[int]:
    """
    Convert a list of strings to a list of integers.

    Args:
        list_of_strings (list[str]): List of strings to be converted.

    Returns:
        list[int]: List of integers converted from strings.
    """
    list_of_ints: list[int] = []
    for element in list_of_strings:
        integer: int = int(element)
        list_of_ints.append(integer)
    return list_of_ints


def _round(value: int | float, number_of_digits: int | None = None) -> int | float:
    """
    Round a value to a given precision in decimal digits.

    Args:
        value (int | float): The number to be rounded.
        number_of_digits (int | None, optional): Number of decimal digits to round to. Defaults to None.

    Returns:
        int | float: The rounded number.

    Raises:
        ValueError: If the type of `value` is not int or float.
    """
    if isinstance(value, int):
        return value
    elif isinstance(value, float):
        if number_of_digits is None:
            return value
        return round(value, number_of_digits)
    else:
        raise ValueError(f"Type '{type(value)}' is not roundable. Use 'int' or 'float'.")


def is_between(value: int | float,
               lower_value: int | float = float('-inf'),
               upper_value: int | float = float('inf'),
               int_only: bool = False,
               float_only: bool = False) -> None:
    """
    Check if a value is between two bounds and numeric.

    Args:
        value (int | float): The value to check.
        lower_value (int | float, optional): The lower bound. Defaults to float('-inf').
        upper_value (int | float, optional): The upper bound. Defaults to float('inf').
        int_only (bool, optional): If True, `value` must be an int. Defaults to False.
        float_only (bool, optional): If True, `value` must be a float. Defaults to False.

    Raises:
        ValueError: If `value` does not meet the type or bound constraints.
    """
    if int_only and not isinstance(value, int):
        raise ValueError(f"Value '{value}' is of instance '{type(value)}'. Use 'int'.")
    if float_only and not isinstance(value, float):
        raise ValueError(f"Value '{value}' is of instance '{type(value)}'. Use 'float'.")
    if not (isinstance(value, int) or isinstance(value, float)):
        raise ValueError(f"Value '{value}' is of instance '{type(value)}'. Use 'int' or 'float'.")
    if not lower_value <= value <= upper_value:
        raise ValueError(f"Value {value} is not between {lower_value} and {upper_value}.")


def none_string(string: str | None) -> str:
    """
    Return an empty string if the input is None.

    Args:
        string (str | None): The input string.

    Returns:
        str: The original string or an empty string if the input was None.
    """
    if string is None:
        return ''
    return string


def to_string(value: int | float | str | None) -> str:
    """
    Convert a value to its string representation.

    Args:
        value (int | float | str | None): The value to convert.

    Returns:
        str: The string representation of the value. Returns '-' if the value is None.
    """
    if value is None:
        return '-'
    elif isinstance(value, int):
        return f'{value}'
    elif isinstance(value, float):
        return f'{round(value, _get_digits())}'
    elif isinstance(value, str):
        return f'{value}'
    try:
        return value.to_string()
    except:
        raise TypeError(f"Type '{type(value)}' is not supported in to_string function.")


def str_is_int(character: str) -> None:
    """
    Check if a given character is a single digit and raise a TypeError if it is not.

    Args:
        character (str): A single character string to check.

    Raises:
        TypeError: If the length of the string is not 1.
        TypeError: If the character is not a digit.
    """
    if len(character) != 1:
        raise TypeError(f"Length of string needs to be exactly 1 '{character}' has {len(character)} characters.")
    integers: set[str] = set([f'{i}' for i in range(10)])
    if not character in integers:
        raise TypeError(f"Character '{character}' is not an integer.")


def str_correct_len(string: str, length: int) -> None:
    """
    Ensure that the given string has the specified length.

    Args:
        string (str): The string to check.
        length (int): The required length of the string.

    Raises:
        TypeError: If the length of the string does not match the specified length.
    """
    if len(string) != length:
        raise TypeError(f"String '{string}' has length {len(string)} but needs to be {length} characters long.")


def get_directory(run: 'Run') -> str:
    """
    Generate the directory path for storing run files based on the run's date.

    Args:
        run (Run): An instance of the Run class, which contains a date attribute.

    Returns:
        str: The directory path in the format './LaTeX/yyyy.mm.dd Run/'.
    """
    string: str = f'./LaTeX/{run.date.__str__(reversed=True, short=True)} Run/'
    return string


def file_exists(file_location: str) -> None:
    if os.path.exists(file_location):
        input("There already is a file. Please backup the following file or it will be deleted:\n" + file_location)
