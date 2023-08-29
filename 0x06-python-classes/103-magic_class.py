#!/usr/bin/python3

import math

class MagicClass:
    """
    This class represents a magic class that calculates properties related to a radius.
    """

    def __init__(self, radius=0):
        """
        Initializes a new MagicClass instance.

        Args:
            radius (number, optional): The radius value. Defaults to 0.

        Raises:
            TypeError: If radius is not a number.
            TypeError: If radius is not an integer or a float.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of a circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of a circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius

    @property
    def radius(self):
        """
        Retrieves the radius attribute.

        Returns:
            number: The radius value.
        """
        return self.__radius

    @radius.setter
    def radius(self, value):
        """
        Sets the radius attribute.

        Args:
            value (number): The new radius value.

        Raises:
            TypeError: If value is not a number.
            TypeError: If value is not an integer or a float.
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError('radius must be a number')
        self.__radius = value

