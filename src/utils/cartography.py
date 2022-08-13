"""
This module contains classes and functions to represent and operate on points
and objects in N-dimensional spaces.
"""

from dataclasses import dataclass
from enum import Enum, auto, unique

@unique
class CardinalDirection(Enum):
    """
    Represents the four different cardinal directions of north, east, south and
    west.
    """
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()

    def rot90_cw(self):
        """
        Returns the CardinalDirection resulting from rotating by 90 degrees in
        the clockwise direction.
        """
        match self:
            case CardinalDirection.NORTH:
                return CardinalDirection.EAST
            case CardinalDirection.EAST:
                return CardinalDirection.SOUTH
            case CardinalDirection.SOUTH:
                return CardinalDirection.WEST
            case CardinalDirection.WEST:
                return CardinalDirection.NORTH
            case _:
                return None

    def rot90_ccw(self):
        """
        Returns the CardinalDirection resulting from rotating by 90 degrees in
        the counter-clockwise direction.
        """
        match self:
            case CardinalDirection.NORTH:
                return CardinalDirection.WEST
            case CardinalDirection.EAST:
                return CardinalDirection.NORTH
            case CardinalDirection.SOUTH:
                return CardinalDirection.EAST
            case CardinalDirection.WEST:
                return CardinalDirection.SOUTH
            case _:
                return None


@dataclass(frozen=True, eq=True)
class Location2D:
    """
    Represents a point location on a two-dimensional plane. Instances of this
    dataclass will be immutable, and can be safely hashed and added to
    collections like dicts (as keys) and sets.
    """
    loc_x: int
    loc_y: int
