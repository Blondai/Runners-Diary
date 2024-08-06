

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
