"""
Solutions for AOC 2017 Day 11.
"""

from src.utils.cartography import Location3D


def process_input_file(filepath="./input/day11.txt"):
    """
    Processes the AOC 2017 Day 11 input file into the format required by the
    solver functions. Returned value is list of comma-separated strings given
    in the input file, representing the moves made by the child process through
    the hex grid.
    """
    with open(filepath, encoding="utf-8") as file:
        return list(file.read().strip().split(","))


def solve_part1(moves):
    """
    Solves AOC 2017 Day 11 Part 1 // Determines the fewest number of steps
    required to reach the child process on the hex grid after all moves have
    been executed.
    """
    cursor = Location3D(0, 0, 0)
    for move in moves:
        match move:
            case "n":
                cursor = Location3D(cursor.loc_x, cursor.loc_y - 1, cursor.loc_z + 1)
            case "ne":
                cursor = Location3D(cursor.loc_x + 1, cursor.loc_y - 1, cursor.loc_z)
            case "se":
                cursor = Location3D(cursor.loc_x + 1, cursor.loc_y, cursor.loc_z - 1)
            case "s":
                cursor = Location3D(cursor.loc_x, cursor.loc_y + 1, cursor.loc_z - 1)
            case "sw":
                cursor = Location3D(cursor.loc_x - 1, cursor.loc_y + 1, cursor.loc_z)
            case "nw":
                cursor = Location3D(cursor.loc_x - 1, cursor.loc_y, cursor.loc_z + 1)
    return calculate_origin_distance_hex(cursor)


def solve_part2(_moves):
    """
    Solves AOC 2017 Day 11 Part 2 // ###
    """
    return NotImplemented


def calculate_origin_distance_hex(location_3d):
    """
    Calculates the distance of the given location on hex grid (represented as
    a three-dimensional point) from the hex grid origin of (0,0,0).
    """
    values = []
    values.append(abs(location_3d.loc_x))
    values.append(abs(location_3d.loc_y))
    values.append(abs(location_3d.loc_z))
    return max(values)
