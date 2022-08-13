"""
Solutions for AOC 2017 Day 21 - "Fractal Art".
"""

import numpy as np


def process_input_file(filepath="./input/day21.txt"):
    """
    Processes the AOC 2017 Day 21 input file into the format required by the
    solver functions. Returns dict with the enhancement rules given in the input
    file.
    """
    with open(filepath, encoding="utf-8") as file:
        rules = {}
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            line = line.replace("/", "")
            groups = line.split(" => ")
            key = groups[0]
            value = groups[1]
            rules[key] = value
        return rules


def solve_part1(rules):
    """
    Solves AOC 2017 Day 21 Part 1 // Determines how many pixels stay on after
    applying five iterations of the enhancement rules.
    """
    artgrid = generate_art(rules, 5)
    return (artgrid == b"#").sum()


def solve_part2(rules):
    """
    Solves AOC 2017 Day 21 Part 2 // Determines how many pixels stay on after
    applying 18 iterations of the enhancement rules.
    """
    artgrid = generate_art(rules, 18)
    return (artgrid == b"#").sum()


def apply_enhancement_rule(rules, old_artgrid, old_unit, new_unit):
    """
    Applies a single iteration of the enhancement rules to the old artgrid,
    returning the new artgrid at the expanded size.
    """
    # Initialise new artgrid as empty
    new_width = (old_artgrid.shape[0] // old_unit) * new_unit
    new_artgrid = np.empty((new_width, new_width), dtype="S1")
    # Consider each square sub-grid with width of old_unit
    for row in range(0, old_artgrid.shape[0], old_unit):
        for col in range(0, old_artgrid.shape[0], old_unit):
            # Create the window grid
            windowgrid = np.empty((old_unit, old_unit), dtype="S1")
            for winx in range(old_unit):
                for winy in range(old_unit):
                    windowgrid[winx][winy] = old_artgrid[row +
                                                         winx][col + winy]
            # Check possible states by combining 90-degree rotations and flips
            flip_rules = [[], [np.fliplr], [np.fliplr, np.flipud], [np.fliplr]]
            match_found = False
            for _ in range(4):
                windowgrid = np.rot90(windowgrid)
                # Apply the flip rules to current rotation and check rule match
                for position_rules in flip_rules:
                    # Apply flips
                    for func in position_rules:
                        windowgrid = func(windowgrid)
                    # Generate string for transformed window grid
                    key = ""
                    for winx in range(old_unit):
                        for winy in range(old_unit):
                            key += windowgrid[winx][winy].decode("utf-8")
                    # Check if transformed window grid matches a rule
                    if key in rules:
                        value = rules[key]
                        # Add the output from matched rule into the new artgrid
                        for winx in range(new_unit):
                            for winy in range(new_unit):
                                i_val = winx * new_unit + winy
                                new_row = row // old_unit * new_unit + winx
                                new_col = col // old_unit * new_unit + winy
                                new_artgrid[new_row][new_col] = value[i_val]
                        match_found = True
                        break
                if match_found:
                    break
                # Put windowgrid back to state before flips were applied
                windowgrid = np.fliplr(windowgrid)
                windowgrid = np.flipud(windowgrid)
    return new_artgrid


def generate_art(rules, iterations):
    """
    Generates the art array by applying the specified number of iterations of
    the rules to the starting pattern (3x3): ".#./..#/###"
    """
    artgrid = np.array([[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]],
                       dtype="S1")
    for _ in range(iterations):
        if artgrid.shape[0] % 2 == 0:
            artgrid = apply_enhancement_rule(rules, artgrid, 2, 3)
        elif artgrid.shape[0] % 3 == 0:
            artgrid = apply_enhancement_rule(rules, artgrid, 3, 4)
    return artgrid
