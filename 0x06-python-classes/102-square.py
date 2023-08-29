#!/usr/bin/python3
"""
This module defines the Square class.
"""

class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (number, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.

        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size attribute.

        Returns:
            number: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size attribute.

        Args:
            value (number): The new size value.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            number: The area of the square.

        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Overrides the equality comparison.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.

        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Overrides the inequality comparison.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.

        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Overrides the less than comparison.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is less than the other square's area, False otherwise.

        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Overrides the less than or equal to comparison.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is less than or equal to the other square's area, False otherwise.

        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Overrides the greater than comparison.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is greater than the other square's area, False otherwise.

        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Overrides the greater than or equal to comparison.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is greater than or equal to the other square's area, False otherwise.

        """
        return self.area() >= other.area()

