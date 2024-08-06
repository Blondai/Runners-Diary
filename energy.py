from utils import _round, is_between


class Energy:
    """
    A class to represent energy in kilocalories and convert it to other units.

    Attributes:
        kcal (int): Energy in kilocalories.
    """
    def __init__(self, kcal: int) -> None:
        """
        Initialize the Energy object with kilocalories.

        Args:
            kcal (int): The energy in kilocalories.

        Raises:
            ValueError: If the provided value is out of the valid range or not an integer.
        """
        is_between(kcal,
                   lower_value=0,
                   int_only=True)
        self.kcal: int = kcal

    @staticmethod
    def from_string(string: str) -> int:
        """
        Create an Energy object from a string representation.

        Args:
            string (str): The string representation of the energy in kilocalories.

        Returns:
            int: The energy in kilocalories.
        """
        kcal: int = int(string)
        return kcal

    def to_kilocalories(self, num_of_digits: int | None = None) -> int:
        """
        Convert the energy to kilocalories.

        Args:
            num_of_digits (int | None, optional): Number of decimal digits to round to. Defaults to None.

        Returns:
            int: The energy in kilocalories.
        """
        kilocalories: int = self.kcal
        return _round(kilocalories, num_of_digits)

    def to_calories(self, num_of_digits: int | None = None) -> float:
        """
        Convert the energy to calories.

        Args:
            num_of_digits (int | None, optional): Number of decimal digits to round to. Defaults to None.

        Returns:
            float: The energy in calories.
        """
        calories: int = self.kcal * 1000
        return _round(calories, num_of_digits)

    def to_joule(self, num_of_digits: int | None = None) -> float:
        """
        Convert the energy to joules.

        Args:
            num_of_digits (int | None, optional): Number of decimal digits to round to. Defaults to None.

        Returns:
            float: The energy in joules.
        """
        joules: float = self.kcal * 4.184
        return _round(joules, num_of_digits)

    def to_kilojoule(self, num_of_digits: int | None = None) -> float:
        """
        Convert the energy to kilojoules.

        Args:
            num_of_digits (int | None, optional): Number of decimal digits to round to. Defaults to None.

        Returns:
            float: The energy in kilojoules.
        """
        kilojoules: float = self.kcal * 4184
        return _round(kilojoules, num_of_digits)
