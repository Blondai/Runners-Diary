from distance import Distance
from duration import Duration
from utils import _round


class Speed:
    """
    A class to represent speed and convert it to different units.

    Attributes:
        distance (Distance): The distance traveled.
        duration (Duration): The time duration of the travel.
    """
    def __init__(self, distance: Distance, duration: Duration) -> None:
        """
        Initialize the Speed object with distance and duration.

        Args:
            distance (Distance): The distance traveled.
            duration (Duration): The time duration of the travel.
        """
        self.distance: Distance = distance
        self.duration: Duration = duration

    def to_kmh(self, num_of_digits: int | None = None) -> float:
        """
        Convert the speed to kilometers per hour.

        Args:
            num_of_digits (int | None, optional): Number of decimal digits to round to. Defaults to None.

        Returns:
            float: The speed in kilometers per hour.
        """
        speed_kmh: float = self.distance.to_kilometers() / self.duration.to_hours()
        return _round(speed_kmh, num_of_digits)

    def to_ms(self, num_of_digits: int | None = None) -> float:
        """
        Convert the speed to meters per second.

        Args:
            num_of_digits (int | None, optional): Number of decimal digits to round to. Defaults to None.

        Returns:
            float: The speed in meters per second.
        """
        speed_ms: float = self.distance.to_meters() / self.duration.to_seconds()
        return _round(speed_ms, num_of_digits)

    def to_mph(self, num_of_digits: int | None = None) -> float:
        """
        Convert the speed to miles per hour.

        Args:
            num_of_digits (int | None, optional): Number of decimal digits to round to. Defaults to None.

        Returns:
            float: The speed in miles per hour.
        """
        speed_mph: float = self.distance.to_miles() / self.duration.to_hours()
        return _round(speed_mph, num_of_digits)

    # TODO: Add Pace Method
    def to_pace(self):
        pass
