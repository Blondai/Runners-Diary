from utils import _round


class Energy:
    def __init__(self, string: str) -> None:
        self.kcal: int = int(string)

    def to_kilocalories(self, num_of_digits: int | None = None) -> int:
        kilocalories: int = self.kcal
        return _round(kilocalories, num_of_digits)

    def to_calories(self, num_of_digits: int | None = None) -> float:
        calories: int = self.kcal * 1000
        return _round(calories, num_of_digits)

    def to_joule(self, num_of_digits: int | None = None) -> float:
        joules: float = self.kcal * 4.184
        return _round(joules, num_of_digits)

    def to_kilojoule(self, num_of_digits: int | None = None) -> float:
        kilojoules: float = self.kcal * 4184
        return _round(kilojoules, num_of_digits)
