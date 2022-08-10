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


@dataclass(frozen=True, eq=True)
class Location2D:
    """
    Represents a point location on a two-dimensional plane. Instances of this
    dataclass will be immutable, and can be safely hashed and added to
    collections like dicts (as keys) and sets.
    """
    loc_x: int
    loc_y: int
