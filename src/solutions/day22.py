"""
Solutions for AOC 2017 Day 22 - "Sporifica Virus".
"""

from copy import deepcopy
from enum import Enum, auto, unique
from src.utils.cartography import CardinalDirection, Location2D


@unique
class NodeState(Enum):
    """
    Represents the different states a node in the computing grid can be in.
    """
    CLEAN = auto()
    WEAKENED = auto()
    INFECTED = auto()
    FLAGGED = auto()

    def next_state(self, is_evolved_virus=False):
        """
        Returns the next state, taking into account the evolved virus if set to
        True.
        """
        match self:
            case NodeState.CLEAN:
                if not is_evolved_virus:
                    return NodeState.INFECTED
                return NodeState.WEAKENED
            case NodeState.WEAKENED:
                return NodeState.INFECTED
            case NodeState.INFECTED:
                if not is_evolved_virus:
                    return NodeState.CLEAN
                return NodeState.FLAGGED
            case NodeState.FLAGGED:
                return NodeState.CLEAN


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
                if char == "#":
                    grid[loc] = NodeState.INFECTED
                elif char == ".":
                    grid[loc] = NodeState.CLEAN
                else:
                    raise ValueError(
                        f"Invalid character in input file: {char}")
                col += 1
            row += 1
        row -= 1
        col -= 1
        centre_loc = Location2D(col // 2 + col % 2, row // 2 + row % 2)
        return (grid, centre_loc)


def solve_part1(grid_data):
    """
    Solves AOC 2017 Day 22 Part 1 // Determines the number of activity bursts by
    the virus carrier that cause a node to become infected, after conducting
    10,000 bursts.
    """
    grid = deepcopy(grid_data[0])
    carrier_loc = grid_data[1]
    infection_bursts = conduct_bursts(grid, carrier_loc, 10000)
    return infection_bursts


def solve_part2(grid_data):
    """
    Solves AOC 2017 Day 22 Part 2 // Determines the number of activity bursts
    by the virus carrier that case a node to become infected, after conducting
    10,000,000 bursts with the evolved virus.
    """
    grid = deepcopy(grid_data[0])
    carrier_loc = grid_data[1]
    infection_bursts = conduct_bursts(grid, carrier_loc, 10000000, True)
    return infection_bursts


def conduct_bursts(grid, start_loc, num_bursts, is_evolved_virus=False):
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
        add_neighbours_to_grid(grid, loc)
        # Check current node state and take actions
        if not is_evolved_virus:
            match grid[loc]:
                case NodeState.INFECTED:
                    direction = direction.rot90_cw()
                case NodeState.CLEAN:
                    # Current location is clean
                    direction = direction.rot90_ccw()
                case _:
                    raise ValueError(f"Invalid NodeState: f{grid[loc]}")
            grid[loc] = grid[loc].next_state(is_evolved_virus)
        else:  # evolved virus
            match grid[loc]:
                case NodeState.CLEAN:
                    direction = direction.rot90_ccw()
                case NodeState.WEAKENED:
                    pass
                case NodeState.INFECTED:
                    direction = direction.rot90_cw()
                case NodeState.FLAGGED:
                    direction = direction.rot90_cw(times=2)
            grid[loc] = grid[loc].next_state(is_evolved_virus)
        # Check if current burst made the location infected
        if grid[loc] == NodeState.INFECTED:
            infection_bursts += 1
        # Move forward one tile in current direction
        loc = direction.update_location(loc)
    return infection_bursts


def add_neighbours_to_grid(grid, loc):
    """
    Adds all neighbours (adjacent and diagonal) of the given 2D-location to the
    grid as CLEAN nodes, if they are not already present.
    """
    for delta_y in (-1, 0, 1):
        for delta_x in (-1, 0, 1):
            surr_loc = Location2D(loc.loc_x + delta_x, loc.loc_y + delta_y)
            if surr_loc not in grid:
                grid[surr_loc] = NodeState.CLEAN
