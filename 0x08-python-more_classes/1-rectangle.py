#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """initialise rectangle class"""

    def __init__(self, width=0, height=0):
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        self.__width = width
        if height < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value
