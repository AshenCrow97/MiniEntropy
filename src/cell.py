#!/usr/bin/env python3

#import typing


class Cell:
    """A class representing a rectangular cell in a grid.

    Attributes
    ----------
    x1, y1 : int
        The coordinates of the top-left corner of the cell.
    x2, y2 : int
        The coordinates of the bottom-right corner of the cell.
    r, g, b, a : int
        The color of the cell in RGBA format.
    """


    def __init__(self, x1 : int, y1 : int, x2 : int, y2 : int, r : int = 0, g : int = 0, b : int = 0, a : int = 0):

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.r = r
        self.g = g
        self.b = b
        self.a = a


    def set_color(self, r : int, g : int, b : int, a : int = 255) -> None:
        """Set color to the cell.

        Parameters
        ----------
        r : int
            The red component of the color.
        g : int
            The green component of the color.
        b : int
            The blue component of the color.
        a : int
            The alpha component of the color.
        """
        
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    
    def width(self) -> int:
        """Return the width of the cell."""

        return self.x2 - self.x1
    

    def height(self) -> int:
        """Return the height of the cell."""

        return self.y2 - self.y1


    def size(self) -> int:
        """Return the size of the cell."""

        return self.width() * self.height()

    
    def __repr__(self):
        """Return a string representation of the cell."""

        return f"Cell({self.x1}, {self.y1}, {self.x2}, {self.y2}, {self.r}, {self.g}, {self.b}, {self.a})"
        

    