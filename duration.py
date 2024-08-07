from utils import string_to_int, _round, is_between


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
        Initialize the Duration object with hours, minutes, and seconds.

        Args:
            hours (int): The hours component of the time.
            minutes (int): The minutes component of the time.
            seconds (int): The seconds component of the time.

        Raises:
            ValueError: If the provided values are out of the valid range or not integers.
        """
        is_between(hours,
                   lower_value=0,
                   int_only=True)
        is_between(minutes,
                   lower_value=0,
                   upper_value=60,
                   int_only=True)
        is_between(seconds,
                   lower_value=0,
                   upper_value=60,
                   int_only=True)
        self.hours: int = hours
        self.minutes: int = minutes
        self.seconds: int = seconds

    @staticmethod
    def from_string(string: str) -> tuple[int, int, int]:
        """
        Create a Duration object from a string representation.

        Args:
            string (str): The string representation of the time, formatted as 'hh:mm:ss' or 'mm:ss'.

        Returns:
            tuple[int, int, int]: A tuple containing hours, minutes, and seconds.

        Raises:
            ValueError: If the string format is incorrect.
        """
        split_string: list[str] = string.split(':')
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
        return hours, minutes, seconds

    @staticmethod
    def from_seconds(seconds: int) -> tuple[int, int, int]:
        """
        Create a Time object from a number of seconds.

        Args:
            seconds (int): The number of seconds.

        Returns:
            tuple[int, int, int]: The hours, minutes, and seconds.
        """
        hours: int = seconds // 3600
        minutes: int = (seconds % 3600) // 60
        seconds: int = seconds % 60
        return hours, minutes, seconds

    @staticmethod
    def from_minutes(minutes: float) -> tuple[int, int, int]:
        """
        Create a Duration object from a number of minutes.

        Args:
            minutes (int): The number of minutes.

        Returns:
            tuple[int, int, int]: The hours, minutes, and seconds.
        """
        hours: int = int(minutes // 60)
        seconds = int((minutes % 1) * 60)
        minutes = int(minutes % 60)
        return hours, minutes, seconds

    @staticmethod
    def from_hours(hours: float) -> tuple[int, int, int]:
        """
        Create a Duration object from a number of hours.

        Args:
            hours (float): The number of hours.

        Returns:
            tuple[int, int, int]: The hours, minutes, and seconds.
        """
        minutes = int((hours - int(hours)) * 60)
        seconds = int((hours * 3600) % 60)
        hours = int(hours)
        return hours, minutes, seconds

    def to_seconds(self, number_of_digits: int | None = None) -> int:
        """
        Convert the duration to total seconds.

        Args:
            number_of_digits (int | None, optional): Number of decimal digits to round to. Defaults to None.

        Returns:
            int: The total time in seconds.
        """
        time_in_seconds: int = 0
        time_in_seconds += self.hours * 3600
        time_in_seconds += self.minutes * 60
        time_in_seconds += self.seconds
        return _round(time_in_seconds, number_of_digits)

    def to_minutes(self, number_of_digits: int | None = None) -> float:
        """
        Convert the duration to total minutes.

        Args:
            number_of_digits (int | None, optional): Number of decimal digits to round to. Defaults to None.

        Returns:
            float: The total time in minutes.
        """
        time_in_minutes: float = 0.0
        time_in_minutes += self.hours * 60
        time_in_minutes += self.minutes
        time_in_minutes += self.seconds / 60
        return _round(time_in_minutes, number_of_digits)

    def to_hours(self, number_of_digits: int | None = None) -> float:
        """
        Convert the duration to total hours.

        Args:
            number_of_digits (int | None, optional): Number of decimal digits to round to. Defaults to None.

        Returns:
            float: The total time in hours.
        """
        time_in_hours: float = 0.0
        time_in_hours += self.hours
        time_in_hours += self.minutes / 60
        time_in_hours += self.seconds / 3600
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
