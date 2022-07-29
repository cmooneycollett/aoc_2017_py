"""
Solutions for AOC 2017 Day 3.
"""


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


def solve_part2(_square_value):
    """
    Solves AOC 2017 Day 3 Part 2 // ###
    """
    return NotImplemented
