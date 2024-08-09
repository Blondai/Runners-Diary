from utils import string_to_int, _round, is_between, str_correct_len, str_is_int


class Duration:
    """
    A class to represent a time duration in hours, minutes, and seconds.

    Attributes:
        hours (int): Hours part of the time.
        minutes (int): Minutes part of the time.
        seconds (int): Seconds part of the time.
    """

    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        """
        Initialize the Duration object with hours, minutes, and seconds. Validates that each value is within the
        appropriate range.

        Args:
            hours (int): The number of hours (must be 0 or greater).
            minutes (int): The number of minutes (must be between 0 and 59).
            seconds (int): The number of seconds (must be between 0 and 59).
        """
        is_between(hours,
                   lower_value=0,
                   int_only=True)
        is_between(minutes,
                   lower_value=0,
                   upper_value=59,
                   int_only=True)
        is_between(seconds,
                   lower_value=0,
                   upper_value=59,
                   int_only=False)
        self.hours: int = hours
        self.minutes: int = minutes
        self.seconds: int = seconds

    @staticmethod
    def from_string(string: str) -> 'Duration':
        """
        Create a Duration object from a string in the format 'hh:mm:ss' or 'mm:ss'.

        Args:
            string (str): The string to convert into a Duration object.

        Returns:
            Duration: A Duration object created from the given string.

        Raises:
            ValueError: If the string does not match the required format.
        """
        split_string: list[str] = string.split(':')
        Duration.ensure_format(split_string)
        list_of_ints: list[int] = string_to_int(split_string)
        if len(list_of_ints) == 2:
            hours: int = 0
            minutes: int = list_of_ints[0]
            seconds: int = list_of_ints[1]
        elif len(list_of_ints) == 3:
            hours: int = list_of_ints[0]
            minutes: int = list_of_ints[1]
            seconds: int = list_of_ints[2]
        else:
            raise ValueError("Incorrect format. Use 'hh:mm:ss' or 'mm:ss'.")
        duration: Duration = Duration(hours, minutes, seconds)
        return duration

    @staticmethod
    def ensure_format(split_string: list[str]) -> None:
        """
        Ensure that each part of the time string has the correct length and is a valid integer.

        Args:
            split_string (list[str]): List of string components from the time string.
        """
        lengths: list[int] = [2, 2, 2]
        for index, string in enumerate(split_string):
            str_correct_len(string, lengths[index])
            for character in string:
                str_is_int(character)

    @staticmethod
    def from_seconds(seconds: int) -> 'Duration':
        """
        Create a Duration object from a total number of seconds.

        Args:
            seconds (float): The total number of seconds.

        Returns:
            Duration: A Duration object representing the given seconds.
        """
        new_hours: int = int(seconds) // 3600
        new_minutes: int = (int(seconds) % 3600) // 60
        new_seconds: int = seconds % 60
        duration: Duration = Duration(new_hours, new_minutes, new_seconds)
        return duration

    @staticmethod
    def from_minutes(minutes: float) -> 'Duration':
        """
        Create a Duration object from a total number of minutes.

        Args:
            minutes (float): The total number of minutes.

        Returns:
            Duration: A Duration object representing the given minutes.
        """
        seconds: int = int(minutes * 60)
        duration: Duration = Duration.from_seconds(seconds)
        return duration

    @staticmethod
    def from_hours(hours: float) -> 'Duration':
        """
        Create a Duration object from a total number of hours.

        Args:
            hours (float): The total number of hours.

        Returns:
            Duration: A Duration object representing the given hours.
        """
        seconds: float = int(hours * 3600)
        duration: Duration = Duration.from_seconds(seconds)
        return duration

    def to_seconds(self, number_of_digits: int | None = None) -> int:
        """
         Convert the Duration to a total number of seconds.

         Args:
             number_of_digits (int | None): Optional rounding precision for the result.

         Returns:
             int: The total number of seconds.
         """
        time_in_seconds: int = 0
        time_in_seconds += self.hours * 3600
        time_in_seconds += self.minutes * 60
        time_in_seconds += self.seconds
        return _round(time_in_seconds, number_of_digits)

    def to_minutes(self, number_of_digits: int | None = None) -> float:
        """
        Convert the Duration to a total number of minutes.

        Args:
            number_of_digits (int | None): Optional rounding precision for the result.

        Returns:
            float: The total number of minutes.
        """
        time_in_minutes: float = self.to_seconds() / 60
        return _round(time_in_minutes, number_of_digits)

    def to_hours(self, number_of_digits: int | None = None) -> float:
        """
         Convert the Duration to a total number of hours.

         Args:
             number_of_digits (int | None): Optional rounding precision for the result.

         Returns:
             float: The total number of hours.
         """
        time_in_hours: float = self.to_seconds() / 3600
        return _round(time_in_hours, number_of_digits)

    def __str__(self, short: bool = False) -> str:
        """
        Return the string representation of the duration in 'hh:mm:ss' or 'mm:ss' format.

        Args:
            short (bool, optional): If True, omit hours if they are zero. Defaults to False.

        Returns:
            str: The string representation of the time.
        """
        if self.hours < 10:
            hours_str: str = f'0{self.hours}'
        else:
            hours_str: str = f'{self.hours}'
        if self.minutes < 10:
            minutes_str: str = f'0{self.minutes}'
        else:
            minutes_str: str = f'{self.minutes}'
        if self.seconds < 10:
            seconds_str: str = f'0{self.seconds}'
        else:
            seconds_str: str = f'{self.seconds}'
        if short and hours_str == '00':
            string: str = minutes_str + ':' + seconds_str
        else:
            string: str = hours_str + ':' + minutes_str + ':' + seconds_str
        return string
