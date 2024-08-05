from utils import string_to_int


class Date:
    def __init__(self, string: str) -> None:
        self.day: int | None = None
        self.month: int | None = None
        self.year: int | None = None
        self.from_string(string)

    def from_string(self, string: str) -> None:
        split_string: list[str] = string.split('.')
        list_of_ints: list[int] = string_to_int(split_string)
        self.day: int = list_of_ints[0]
        self.month: int = list_of_ints[1]
        self.year: int = list_of_ints[2]

    def __str__(self, reversed: bool = False) -> str:
        if self.day < 10:
            day_string: str = f'0{self.day}'
        else:
            day_string: str = f'{self.day}'
        if self.month < 10:
            month_string: str = f'0{self.month}'
        else:
            month_string: str = f'{self.month}'
        year_string: str = f'0{self.year}'
        if not reversed:  # Use dd.mm.yyyy
            return f'{day_string}.{month_string}.{year_string}'
        else:  # Use yyyy.mm.dd
            return f'{year_string}.{month_string}.{day_string}'
