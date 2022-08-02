"""
This module contains classes and functions to represent and operate on points
and objects in N-dimensional spaces.
"""

from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Location2D:
    """
    Represents a point location on a two-dimensional plane. Instances of this
    dataclass will be immutable, and can be safely hashed and added to
    collections like dicts (as keys) and sets.
    """
    loc_x: int
    loc_y: int


@dataclass(frozen=True, eq=True)
class Location3D:
    """
    Represents a point location on a three-dimensional plane. Instances of this
    dataclass will be immutable, and can be safely hashed and added to
    collections like dicts (as keys) and sets.
    """
    loc_x: int
    loc_y: int
    loc_z: int
