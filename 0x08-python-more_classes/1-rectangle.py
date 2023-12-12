#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """initialise rectangle class"""

    def __init__(self, width=0, height=0):
        if width < 0:
            raise TypeError("width must be >= 0")
        if not isinstance(width, int):
            raise ValueError("width must be an integer")
        self.__width = width
        if height < 0:
            raise TypeError("height must be >= 0")
        if not isinstance(height, int):
            raise ValueError("height must be an integer")
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
