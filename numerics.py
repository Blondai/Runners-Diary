
class Integer:
    def __init__(self, integer: int | None) -> None:
        """
        Initialize the Integer object.

        Args:
            integer (int | None): An integer value or None.
        """
        self.integer: int | None = integer

    def __str__(self) -> str:
        """
        Return the string representation of the Integer object.

        If the integer is None, return '-'.
        Otherwise, return the string representation of the integer.

        Returns:
            str: String representation of the integer or '-'.
        """
        if not self.integer is None:
            string: str = str(self.integer)
            return string
        return '-'

    def __rmul__(self, other: float | int) -> float | int:
        """
        Multiply the Integer object by another number (reversed multiplication).

        Args:
            other (float | int): The number to multiply by.

        Returns:
            float | int: The result of the multiplication.
        """
        return self.integer * other

    def __mul__(self, other: float | int) -> float | int:
        """
        Multiply the Integer object by another number.

        Args:
            other (float | int): The number to multiply by.

        Returns:
            float | int: The result of the multiplication.
        """
        return self.integer * other

    @staticmethod
    def from_string(string: str) -> 'Integer':
        """
        Convert a string to an Integer object.

        If the string is empty, set the integer to None. Otherwise, convert the string to an integer.

        Args:
            string (str): The string to convert.

        Returns:
            Integer: An Integer object with the parsed value.
        """
        if string == '' or string == '-':
            integer: None = None
        else:
            integer: int = int(string)
        return Integer(integer)


class Floating:
    def __init__(self, floating: float | None) -> None:
        """
         Initialize the Floating object.

         Args:
             floating (float | None): A floating-point value or None.
         """
        self.floating: float | None = floating

    def __str__(self) -> str:
        """
         Return the string representation of the Floating object.

         If the floating value is None, return '-'. Otherwise, return the string representation of the floating-point
         value.

         Returns:
             str: String representation of the floating-point value or '-'.
         """
        if not self.floating is None:
            string: str = str(self.floating)
            return string
        return '-'

    def __rmul__(self, other: float | int) -> float:
        """
        Multiply the Floating object by another number (reversed multiplication).

        Args:
            other (float | int): The number to multiply by.

        Returns:
            float: The result of the multiplication.
        """
        return self.floating * other

    def __mul__(self, other: float | int) -> float:
        """
        Multiply the Floating object by another number.

        Args:
            other (float | int): The number to multiply by.

        Returns:
            float: The result of the multiplication.
        """
        return self.floating * other

    @staticmethod
    def from_string(string: str) -> 'Floating':
        """
        Convert a string to a Floating object.

        If the string is empty, set the floating value to None. Otherwise, convert the string to a float.

        Args:
            string (str): The string to convert.

        Returns:
            Floating: A Floating object with the parsed value.
        """
        if string == '' or string == '-':
            floating: None = None
        else:
            floating: float = float(string)
        return Floating(floating)
