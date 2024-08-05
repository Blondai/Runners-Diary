from utils import string_to_int, _round


class Time:
    def __init__(self, string: str) -> None:
        self.hours: int | None = None
        self.minutes: int | None = None
        self.seconds: int | None = None
        self.from_string(string)

    def from_string(self, string: str) -> None:
        split_string: list[str] = string.split(':')
        list_of_ints: list[int] = string_to_int(split_string)
        if len(list_of_ints) == 2:
            self.hours: int = 0
            self.minutes: int = list_of_ints[0]
            self.seconds: int = list_of_ints[1]
        elif len(list_of_ints) == 3:
            self.hours: int = list_of_ints[0]
            self.minutes: int = list_of_ints[1]
            self.seconds: int = list_of_ints[2]
        else:
            raise ValueError("Incorrect format. Use 'hh:mm:ss' or 'mm:ss'.")

    def to_seconds(self, number_of_digits: int | None = None) -> int:
        time_in_seconds: int = 0
        time_in_seconds += self.hours * 3600
        time_in_seconds += self.minutes * 60
        time_in_seconds += self.seconds
        return _round(time_in_seconds, number_of_digits)

    def to_minutes(self, number_of_digits: int | None = None) -> float:
        time_in_minutes: float = 0.0
        time_in_minutes += self.hours * 60
        time_in_minutes += self.minutes
        time_in_minutes += self.seconds / 60
        return _round(time_in_minutes, number_of_digits)

    def to_hours(self, number_of_digits: int | None = None) -> float:
        time_in_hours: float = 0.0
        time_in_hours += self.hours
        time_in_hours += self.minutes / 60
        time_in_hours += self.seconds / 3600
        return _round(time_in_hours, number_of_digits)

    def __str__(self) -> str:
        string: str = ''
        if self.hours < 10:
            string += f'0{self.hours}:'
        else:
            string += f'{self.hours}:'
        if self.minutes < 10:
            string += f'0{self.minutes}:'
        else:
            string += f'{self.minutes}:'
        if self.seconds < 10:
            string += f'0{self.seconds}'
        else:
            string += f'{self.seconds}'
        return string
