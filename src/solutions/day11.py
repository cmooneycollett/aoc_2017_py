"""
Solutions for AOC 2017 Day 11.
"""


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
    location = (0, 0, 0)
    for move in moves:
        match move:
            case "n":
                location = (location[0], location[1] - 1, location[2] + 1)
            case "ne":
                location = (location[0] + 1, location[1] - 1, location[2])
            case "se":
                location = (location[0] + 1, location[1], location[2] - 1)
            case "s":
                location = (location[0], location[1] + 1, location[2] - 1)
            case "sw":
                location = (location[0] - 1, location[1] + 1, location[2])
            case "nw":
                location = (location[0] - 1, location[1], location[2] + 1)
    return calculate_origin_distance_hex(location)


def solve_part2(moves):
    """
    Solves AOC 2017 Day 11 Part 2 // Determines the furthest away from hex grid
    origin that the child process gets at any point of executing the given
    moves, starting at the hex grid origin.
    """
    location = (0, 0, 0)
    max_distance = 0
    for move in moves:
        match move:
            case "n":
                location = (location[0], location[1] - 1, location[2] + 1)
            case "ne":
                location = (location[0] + 1, location[1] - 1, location[2])
            case "se":
                location = (location[0] + 1, location[1], location[2] - 1)
            case "s":
                location = (location[0], location[1] + 1, location[2] - 1)
            case "sw":
                location = (location[0] - 1, location[1] + 1, location[2])
            case "nw":
                location = (location[0] - 1, location[1], location[2] + 1)
        distance = calculate_origin_distance_hex(location)
        if distance > max_distance:
            max_distance = distance
    return max_distance


def calculate_origin_distance_hex(location_3d):
    """
    Calculates the distance of the given location on hex grid (represented as
    a three-dimensional point) from the hex grid origin of (0,0,0).
    """
    return max(abs(dim) for dim in location_3d)
