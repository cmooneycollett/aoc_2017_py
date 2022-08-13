"""
Solutions for AOC 2017 Day 22 - "Sporifica Virus".
"""

from copy import deepcopy
from src.utils.cartography import CardinalDirection, Location2D


def process_input_file(filepath="./input/day22.txt"):
    """
    Processes the AOC 2017 Day 22 input file into the format required by the
    solver functions. Returns tuple containing: dict with the locations and
    contents given in the input file, taking the top-left location as (0,0); and
    location of the centre of the input grid.
    """
    with open(filepath, encoding="utf-8") as file:
        row = 0
        col = 0
        grid = {}   # Key: location, value: is the location infected (bool)
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            col = 0
            for char in line:
                loc = Location2D(col, row)
                grid[loc] = (char == "#")
                col += 1
            row += 1
        row -= 1
        col -= 1
        centre_loc = Location2D(col // 2 + col % 2, row // 2 + row % 2)
        return (grid, centre_loc)


def solve_part1(grid_data):
    """
    Solves AOC 2017 Day 22 Part 1 // Determines the number of activity bursts by
    the virus carrier that cause a node to become infected.
    """
    grid = deepcopy(grid_data[0])
    carrier_loc = grid_data[1]
    infection_bursts = conduct_activity_bursts(grid, carrier_loc, 10000)
    return infection_bursts


def solve_part2(_grid_data):
    """
    Solves AOC 2017 Day 22 Part 2 // ###
    """
    return NotImplemented


def conduct_activity_bursts(grid, start_loc, num_bursts):
    """
    Updates the grid by conducting the specified number of activity bursts for
    the virus carrier. Returns the number of bursts that cause a node to become
    infected.
    """
    direction = CardinalDirection.NORTH
    loc = start_loc
    infection_bursts = 0
    for _ in range(num_bursts):
        # Add surrounding nodes if not already in the grid
        for delta_y in (-1, 0, 1):
            for delta_x in (-1, 0, 1):
                surr_loc = Location2D(loc.loc_x + delta_x, loc.loc_y + delta_y)
                if surr_loc not in grid:
                    grid[surr_loc] = False
        # Check current node state and take actions
        if grid[loc]:
            # Current location is infected
            direction = direction.rot90_cw()
            grid[loc] = False
        else:
            # Current location is clean
            direction = direction.rot90_ccw()
            grid[loc] = True
            infection_bursts += 1
        # Move forward one tile in current direction
        match direction:
            case CardinalDirection.NORTH:
                loc = Location2D(loc.loc_x, loc.loc_y - 1)
            case CardinalDirection.EAST:
                loc = Location2D(loc.loc_x + 1, loc.loc_y)
            case CardinalDirection.SOUTH:
                loc = Location2D(loc.loc_x, loc.loc_y + 1)
            case CardinalDirection.WEST:
                loc = Location2D(loc.loc_x - 1, loc.loc_y)
    return infection_bursts
