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


def _round(value: int | float, number_of_digits: int | None = None) -> int | float | None:
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
    if value is None:
        return None
    elif isinstance(value, int):
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
    Check if a value is between two bounds and numeric or None.

    Args:
        value (int | float): The value to check.
        lower_value (int | float, optional): The lower bound. Defaults to float('-inf').
        upper_value (int | float, optional): The upper bound. Defaults to float('inf').
        int_only (bool, optional): If True, `value` must be an int. Defaults to False.
        float_only (bool, optional): If True, `value` must be a float. Defaults to False.

    Raises:
        ValueError: If `value` does not meet the type or bound constraints.
    """
    if value is None:
        return
    if int_only and not isinstance(value, int):
        raise ValueError(f"Value '{value}' is of instance '{type(value)}'. Use 'int'.")
    if float_only and not isinstance(value, float):
        raise ValueError(f"Value '{value}' is of instance '{type(value)}'. Use 'float'.")
    if not (isinstance(value, int) or isinstance(value, float)):
        raise ValueError(f"Value '{value}' is of instance '{type(value)}'. Use 'int' or 'float'.")
    if not lower_value <= value <= upper_value:
        raise ValueError(f"Value {value} is not between {lower_value} and {upper_value}.")


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
    elif value == '':
        return '$-$'
    elif isinstance(value, int):
        return f'{_decimal_separator(value)}'
    elif isinstance(value, float):
        return f'{_decimal_separator(round(value, _get_digits()))}'
    elif isinstance(value, str):
        return f'{value}'
    try:
        return value.to_string()
    except:
        raise TypeError(f"Type '{type(value)}' is not supported in to_string function.")


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
    """
    Check if a file exists at the specified location and prompt the user to back up the file if it does.

    Args:
        file_location (str): The path to the file to check.
    """
    if os.path.exists(file_location):
        input("There already is a file. Please back up the following file or it will be deleted:\n" + file_location)


def _decimal_separator_int(integer: int) -> str:
    """
    Format an integer with decimal separators for thousands.

    Args:
        integer (int): The integer to format.

    Returns:
        str: The formatted string with decimal separators.
    """
    string: str = str(integer)[::-1]
    formated_string: str = ''
    for (index, character) in enumerate(string):
        formated_string += character
        if (index + 1) % 3 == 0 and index + 1 != len(string):
            formated_string += r' ,\ '
    return formated_string[::-1]


def _decimal_separator_float(floating: float) -> str:
    """
    Format a float with decimal separators for thousands and include the decimal part.

    Args:
        floating (float): The float to format.

    Returns:
        str: The formatted string with decimal separators and decimal part.
    """
    decimal_part: str = '.' + str(floating).split('.')[1]
    formated_string = _decimal_separator_int(int(floating))
    formated_string += decimal_part
    return formated_string


def _decimal_separator(number: int | float) -> str:
    """
    Format a number (int or float) with decimal separators.

    Args:
        number (int | float): The number to format.

    Returns:
        str: The formatted string with decimal separators.

    Raises:
        ValueError: If the input is neither an integer nor a float.
    """
    if isinstance(number, int):
        string: str = _decimal_separator_int(number)
        return string
    elif isinstance(number, float):
        string: str = _decimal_separator_float(number)
        return string
    else:
        raise ValueError(f"Can only convert 'int' or 'float'. Type '{type(number)}' was commited.")


def _new_folder(folder: str) -> None:
    """
    Create a new folder if it does not exist.

    Args:
        folder (str): The folder path.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)
    else:
        input("Folder already exists. Backup any important files. Press enter to continue.")
