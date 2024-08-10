from utils import string_to_int, is_between


class Date:
    """
    A class to represent a date and provide string conversion.

    Attributes:
        day (int): Day of the month.
        month (int): Month of the year.
        year (int): Year.
    """

    def __init__(self, day: int, month: int, year: int) -> None:
        """
        Initialize the Date object with day, month, and year.

        Args:
            day (int): The day of the month.
            month (int): The month of the year.
            year (int): The year.

        Raises:
            ValueError: If the provided values are out of the valid range or not integers.
        """
        is_between(day,
                   lower_value=1,
                   upper_value=31,
                   int_only=True)
        is_between(month,
                   lower_value=1,
                   upper_value=12,
                   int_only=True)
        is_between(year,
                   lower_value=0,
                   int_only=True)
        self.day: int = day
        self.month: int = month
        self.year: int = year

    @staticmethod
    def from_string(string: str) -> 'Date':
        """
        Create a Date object from a string in the format 'dd.mm.yyyy'.

        Args:
            string (str): The date string to convert, formatted as 'dd.mm.yyyy'.

        Returns:
            Date: A Date object created from the given string.
        """
        split_string: list[str] = string.split('.')
        list_of_ints: list[int] = string_to_int(split_string)
        day: int = list_of_ints[0]
        month: int = list_of_ints[1]
        year: int = list_of_ints[2]
        date: Date = Date(day, month, year)
        return date

    def __str__(self, reversed: bool = False, short: bool = False) -> str:
        """
        Return the string representation of the date.

        Args:
            reversed (bool, optional): Whether to reverse the date format to 'yyyy.mm.dd' or 'yy.mm.dd'. Defaults to
            False.
            short (bool, optional): Whether to use the short year format 'yy'. Defaults to False.

        Returns:
            str: The string representation of the date.
        """
        if self.day < 10:  # Add leading zero
            day_string: str = f'0{self.day}'
        else:
            day_string: str = f'{self.day}'
        if self.month < 10:  # Add leading zero
            month_string: str = f'0{self.month}'
        else:
            month_string: str = f'{self.month}'
        year_string_long: str = f'{self.year}'
        year_string_short: str = f'{self.year}'[2:4]
        if not reversed and not short:  # Use dd.mm.yyyy
            return f'{day_string}.{month_string}.{year_string_long}'
        elif not reversed and short:  # Use dd.mm.yy
            return f'{day_string}.{month_string}.{year_string_short}'
        elif reversed and not short:  # Use yyyy.mm.dd
            return f'{year_string_long}.{month_string}.{day_string}'
        elif reversed and short:  # Use yy.mm.dd
            return f'{year_string_short}.{month_string}.{day_string}'
