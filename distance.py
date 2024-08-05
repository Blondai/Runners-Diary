from utils import _round


class Distance:
    def __init__(self, string: str) -> None:
        self.distance_meter: int = int(string)

    def to_meter(self, num_of_digits: int | None = None) -> int:
        meter: int = self.distance_meter
        return _round(meter, num_of_digits)

    def to_kilometer(self, num_of_digits: int | None = None) -> float:
        kilometer: float = self.distance_meter * 1000
        return _round(kilometer, num_of_digits)

    def to_megameter(self, num_of_digits: int | None = None) -> float:
        megameter: float = self.distance_meter / (1000 * 1000)
        return _round(megameter, num_of_digits)

    def to_miles(self, num_of_digits: int | None = None) -> float:
        miles: float = self.distance_meter * (1000 * 1.609344)
        return _round(miles, num_of_digits)

    def to_feet(self, num_of_digits: int | None = None) -> float:
        feet: float = self.distance_meter * (1 / 0.3048)
        return _round(feet, num_of_digits)
