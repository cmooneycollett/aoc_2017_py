"""
Solutions for AOC 2017 Day 19 - "A Series of Tubes".
"""

from src.utils.cartography import CardinalDirection, Location2D


def process_input_file(filepath="./input/day19.txt"):
    """
    Processes the AOC 2017 Day 19 input file into the format required by the
    solver functions. Returned value is dict with locations mapped to the
    element present at that location (letter, "-", "|" or "+").
    """
    routing_map = {}
    with open(filepath, encoding="utf-8") as file:
        row = 0
        for line in file.readlines():
            col = 0
            for char in line:
                if not char.isspace():
                    loc = Location2D(col, row)
                    routing_map[loc] = char
                col += 1
            row += 1
    return routing_map


def solve_part1(routing_map):
    """
    Solves AOC 2017 Day 19 Part 1 // Determines the letters (in order) that the
    packet will find as it follows the path in the routing map.
    """
    (letters, _) = follow_routing_map(routing_map)
    return letters


def solve_part2(_routing_map):
    """
    Solves AOC 2017 Day 19 Part 2 // ###
    """
    return NotImplemented


def follow_routing_map(routing_map):
    """
    Follows the path in the routing map, returning the letters seen (in order)
    and the steps taken as a tuple.
    """
    steps = 0
    direction = CardinalDirection.SOUTH
    # Determine starting location - only line connected in top row of map
    loc = [loc for loc in routing_map if loc.loc_y == 0][0]
    letters = []
    while True:
        steps += 1
        if routing_map[loc].isalpha():
            letters.append(routing_map[loc])
        elif routing_map[loc] == "+":
            # Check packet direction on corner tile
            routes = []  # Two routes expected from "+" location
            for (delta_x, delta_y, check_dirn) in [
                    (1, 0, CardinalDirection.EAST), (0, 1, CardinalDirection.SOUTH),
                    (-1, 0, CardinalDirection.WEST), (0, -1, CardinalDirection.NORTH)]:
                check_loc = Location2D(
                    loc.loc_x + delta_x, loc.loc_y + delta_y)
                if check_loc in routing_map:
                    routes.append(check_dirn)
            match direction:
                case CardinalDirection.NORTH:
                    direction = [dirn for dirn in routes if dirn !=
                                 CardinalDirection.SOUTH][0]
                case CardinalDirection.EAST:
                    direction = [dirn for dirn in routes if dirn !=
                                 CardinalDirection.WEST][0]
                case CardinalDirection.SOUTH:
                    direction = [dirn for dirn in routes if dirn !=
                                 CardinalDirection.NORTH][0]
                case CardinalDirection.WEST:
                    direction = [dirn for dirn in routes if dirn !=
                                 CardinalDirection.EAST][0]
        # Move the packet based on current direction
        match direction:
            case CardinalDirection.NORTH:
                loc = Location2D(loc.loc_x, loc.loc_y - 1)
            case CardinalDirection.EAST:
                loc = Location2D(loc.loc_x + 1, loc.loc_y)
            case CardinalDirection.SOUTH:
                loc = Location2D(loc.loc_x, loc.loc_y + 1)
            case CardinalDirection.WEST:
                loc = Location2D(loc.loc_x - 1, loc.loc_y)
        # Check if end of routing map has been reached
        if loc not in routing_map:
            break
    return ("".join(letters), steps)
