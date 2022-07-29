"""
Solutions for AOC 2017 Day 3.
"""

from src.utils.cartography import Location2D


def process_input_file():
    """
    Processes the AOC 2017 Day 3 input file into the format required by the
    solver functions. Returned value is the square value given in the input
    file.
    """
    with open("./input/day03.txt", encoding="utf-8") as file:
        return int(file.read().strip())


def solve_part1(square_value):
    """
    Solves AOC 2017 Day 3 Part 1 // Determines the Manhattan distance of the
    given square value from the spiral origin when generating the simple spiral.
    """
    (loc_x, loc_y) = (0, 0)
    (delta_x, delta_y) = (1, 0)
    cell_value = 1
    ring = 0
    ring_base = 1
    while cell_value < square_value:
        cell_value += 1
        loc_x += delta_x
        loc_y += delta_y
        # Adjust the direction of spiral when entering new ring or corner
        if cell_value == ring_base + 1:
            delta_x = 0
            delta_y = -1
            ring += 1
            ring_base = pow(2 * ring + 1, 2)
        elif cell_value == ring_base - (8 * ring) / 4 * 3:
            delta_x = -1
            delta_y = 0
        elif cell_value == ring_base - (8 * ring) / 4 * 2:
            delta_x = 0
            delta_y = 1
        elif cell_value == ring_base - (8 * ring) / 4:
            delta_x = 1
            delta_y = 0
    # Return Manhattan distance of resulting location
    return abs(loc_x) + abs(loc_y)


def solve_part2(square_value):
    """
    Solves AOC 2017 Day 3 Part 2 // Determines the first value written that is
    larger than the given square value when using the complex spiral generation
    method.
    """
    last_loc = Location2D(0, 0)
    spiral = {last_loc: 1}
    delta_x = 1
    delta_y = 0
    ring = 0
    ring_base = 1
    cell_serial = 1  # Track how many cells have been allocated
    while spiral[last_loc] < square_value:
        # Update last location and cell serial number
        last_loc = Location2D(
            last_loc.loc_x + delta_x, last_loc.loc_y + delta_y)
        cell_serial += 1
        # Calculate cell value as sum of its allocated neighbours
        cell_value = 0
        for shift_y in (-1, 0, 1):
            for shift_x in (-1, 0, 1):
                if shift_x == 0 and shift_y == 0:
                    continue
                check_loc = Location2D(
                    last_loc.loc_x + shift_x, last_loc.loc_y + shift_y)
                if check_loc in spiral:
                    cell_value += spiral[check_loc]
        spiral[last_loc] = cell_value
        # Adjust the direction of spiral when entering new ring or corner
        if cell_serial == ring_base + 1:
            delta_x = 0
            delta_y = -1
            ring += 1
            ring_base = pow(2 * ring + 1, 2)
        elif cell_serial == ring_base - (8 * ring) / 4 * 3:
            delta_x = -1
            delta_y = 0
        elif cell_serial == ring_base - (8 * ring) / 4 * 2:
            delta_x = 0
            delta_y = 1
        elif cell_serial == ring_base - (8 * ring) / 4:
            delta_x = 1
            delta_y = 0
    return spiral[last_loc]
