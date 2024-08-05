def string_to_int(list_of_strings: list[str]) -> list[int]:
    list_of_ints: list[int] = []
    for element in list_of_strings:
        integer: int = int(element)
        list_of_ints.append(integer)
    return list_of_ints


def _round(value: int | float, number_of_digits: int | None = None) -> int | float:
    if isinstance(value, int):
        return value
    elif isinstance(value, float):
        if number_of_digits is None:
            return value
        return round(value, number_of_digits)
    else:
        raise ValueError(f"Type '{type(value)}' is not roundable. Use 'int' or 'float'.")
