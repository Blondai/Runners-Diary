from utils import _round, is_between


class Distance:
    """
    A class to represent distance in meters and convert it to other units.

    Attributes:
        distance_meters (int): Distance in meters.
    """

    def __init__(self, distance_meters: int | None) -> None:
        """
        Initialize the Distance object with meters.

        Args:
            distance_meters (int): The distance in meters.

        Raises:
            ValueError: If the provided value is out of the valid range or not an integer.
        """
        is_between(distance_meters,
                   lower_value=0,
                   int_only=True)
        self.distance_meters: int | None = distance_meters

    def __str__(self) -> str:
        """
        Return a string representation of the Distance object.

        Returns:
            str: The string representation of the distance.
        """
        if not self.distance_meters is None:
            string: str = f'{self.distance_meters}'
            return string
        return '-'

    @staticmethod
    def from_string(string: str) -> 'Distance':
        """
        Create a Distance object from a string representing the distance in meters.

        Args:
            string (str): The distance string to convert, containing only digits.

        Returns:
            Distance: A Distance object created from the given string.
        """
        if string == '' or string == '-':
            distance_meter: None = None
        else:
            distance_meter: int = int(string)
        distance: Distance = Distance(distance_meter)
        return distance

    def to_meters(self, num_of_digits: int | None = None) -> int:
        """
        Convert the distance to meters.

        Args:
            num_of_digits (int | None, optional): Number of decimal digits to round to. Defaults to None.

        Returns:
            int: The distance in meters.
        """
        meters: int = self.distance_meters
        return _round(meters, num_of_digits)

    def to_kilometers(self, num_of_digits: int | None = None) -> float:
        """
        Convert the distance to kilometers.

        Args:
            num_of_digits (int | None, optional): Number of decimal digits to round to. Defaults to None.

        Returns:
            float: The distance in kilometers.
        """
        kilometers: float = self.distance_meters / 1000
        return _round(kilometers, num_of_digits)

    def to_megameters(self, num_of_digits: int | None = None) -> float:
        """
        Convert the distance to megameters.

        Args:
            num_of_digits (int | None, optional): Number of decimal digits to round to. Defaults to None.

        Returns:
            float: The distance in megameters.
        """
        megameters: float = self.distance_meters / (1000 * 1000)
        return _round(megameters, num_of_digits)

    def to_miles(self, num_of_digits: int | None = None) -> float:
        """
        Convert the distance to miles.

        Args:
            num_of_digits (int | None, optional): Number of decimal digits to round to. Defaults to None.

        Returns:
            float: The distance in miles.
        """
        miles: float = self.distance_meters * (1000 * 1.609344)
        return _round(miles, num_of_digits)

    def to_feet(self, num_of_digits: int | None = None) -> float:
        """
        Convert the distance to feet.

        Args:
            num_of_digits (int | None, optional): Number of decimal digits to round to. Defaults to None.

        Returns:
            float: The distance in feet.
        """
        feet: float = self.distance_meters * (1 / 0.3048)
        return _round(feet, num_of_digits)
